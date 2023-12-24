const str1 = "xxoo"; // true
const str2 = "xxxoo"; // false
const str3 = "xXoo"; // true

function XO(str) {
	xs = 0;
	os = 0;
	str = str
		.toLowerCase()
		.split("")
		.map((l) => {
			if (l == "x") xs += 1;
			if (l == "o") os += 1;
		});

	if (xs == os) return true;

	return false;
}

console.log(XO(str1));
console.log(XO(str2));
console.log(XO(str3));
