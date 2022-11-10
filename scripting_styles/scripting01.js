let map_level = ['1~first floor',
				 '1~roof',
				 '2~basement',]


let struct_map = map_level.reduce((a, i) => {
	let [map, level] = i.split('~')
	if(a[map]) {
		a[map].push(level)
	}else {
		a[map] = [level]
	}
	return a
}, {})

struct_map = map_level.reduce((a, i)=>([map,level]=i.split('~'), a[map]=a[map]||[], a[map].push(level), a), {}) // js scripting style - (a[map] = a[map] || []) - idempotence

console.log(struct_map)