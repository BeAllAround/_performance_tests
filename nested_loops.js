function linear_nested(size) {
	let arr = []

	let i
	for(i = 0; i < size; i++) {
		arr.push(i)
	}


	let start = Date.now()
	for(let item of arr) {
		arr.find(v=>v==item)
	}
	console.log("linear passed: ", (Date.now() - start) / 1000)
	// O(n^2)
}

function hash_nested() {	
	let arr = []

	let i
	for(i = 0; i < size; i++) {
		arr.push(i)
	}

	let arr_hash = arr.reduce((obj, v) => Object.assign(obj, 
		{[v]: true,}), {})
	// console.log(Object.keys(arr_hash).length)

	let start = Date.now()
	for(let item of arr) {
		arr_hash[item]
	}
	console.log("hash passed: ", (Date.now() - start) / 1000)
	// O(n+n)
}

const size = 10000
linear_nested(size)
hash_nested(size)
