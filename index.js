const { ethers } = require('ethers')
const { MerkleTree } = require('merkletreejs')
const { keccak256 } = ethers//.utils
const fs = require('fs')

const args = process.argv.slice(2)
let csv_path = args[0]
let out_dir = args[1]

fs.readFile(csv_path, 'utf8', (err, data) => {

  // load wl from file
  let whitelist = data.split('\n').map(r => r.split(',')[0].trim())

  // get tree
  let leaves = whitelist.map((addr) => keccak256(addr))
  let tree = new MerkleTree(leaves, keccak256, { sortPairs: true })
  let root = tree.getHexRoot()
  console.log('root: ' + root)

  // separate wl by first char after 0x
  let chunk = {}
  let from_time = new Date()
  whitelist.forEach(addr => {
    // gen proof
    let leaf = keccak256(addr)
    let proof = tree.getHexProof(leaf)
    // add to chunk
    let l = addr.toLowerCase()
    let s = l[2]
    if (!chunk[s]) chunk[s] = {}
    chunk[s][l] = proof
  })
  let usage_time = (new Date()) - from_time
  console.log('usage time: ' + (usage_time / 1_000) + 's')

  // debug
  // let sum = 0
  // console.log(chunk)
  // console.log(whitelist.length)
  // for (k in chunk) {
  //   let size = Object.keys(chunk[k]).length
  //   console.log(k, size)
  //   sum += size
  // }
  // console.log(sum)

  // write to file
  for (k in chunk) {
    let content = JSON.stringify(chunk[k])
    let out_path = `./${out_dir}/${k}.js`
    fs.writeFile(out_path, content, 'utf8', (err) => {
      if (err)
        console.error(out_path, err);
      else
        console.log(out_path, 'OK');
    })
  }

})
