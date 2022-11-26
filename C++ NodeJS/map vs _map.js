
function _map(arr, callback) {
	let a = []
	for(let item of arr)
		a.push(callback(item))
	return a
}

// Array.prototype.map // written in C++ and thus a bit faster
let arr = []
arr.length = 100000
arr.fill(0)

let start = Date.now()
arr.map(v=>v+1)
// _map(arr, v=>v+1)
console.log('CPU: ', (Date.now() - start)/1000)
