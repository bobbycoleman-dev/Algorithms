const a1 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"];
const a2 = ["NORTH", "WEST", "SOUTH", "EAST"];
const a3 = ["NORTH", "SOUTH", "EAST", "WEST", "EAST", "WEST"];

function dirReduc(arr) {
	const re = /NORTHSOUTH|SOUTHNORTH|EASTWEST|WESTEAST/gi;

	for (let i = 0; i < arr.length; i++) {
		if (`${arr[i]}${arr[i + 1]}`.match(re)) {
			arr.splice(i, 2);
			i -= 2;
		}
	}

	return arr;
}

console.log(dirReduc(a1));
console.log(dirReduc(a2));
console.log(dirReduc(a3));
