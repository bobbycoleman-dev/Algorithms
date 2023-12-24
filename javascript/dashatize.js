/*
Given an integer, return a string with dash '-' marks before and after each odd digit, but do not begin or end the string with a dash mark.

Ex:

274 -> '2-7-4'
6815 -> '68-1-5'
*/

num1 = 274;
num2 = 6829;
num3 = 5311;
num4 = -73437;

function dashatize(num) {
	let str = Math.abs(num).toString().split("");
	let result = "";

	for (let i = 0; i < str.length; i++) {
		if (Number(str[i]) % 2 != 0) {
			if (Number(str[i - 1]) % 2 == 0) {
				result += `-${str[i]}-`;
			} else {
				result += `${str[i]}-`;
			}
		} else {
			result += str[i];
		}
	}

	if (result[result.length - 1] == "-") {
		result = result.slice(0, -1);
	}

	return result;
}

console.log(dashatize(num1));
console.log(dashatize(num2));
console.log(dashatize(num3));
console.log(dashatize(num4));
