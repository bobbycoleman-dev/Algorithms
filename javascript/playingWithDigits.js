function digPow(n, p) {
	let arr = n
		.toString()
		.split("")
		.map((num) => parseInt(num));
	let sum = 0;
	for (let i = 0; i < arr.length; i++) {
		sum += arr[i] ** (p + i);
	}

	let answer = sum / n;

	if (answer - Math.floor(answer) !== 0) {
		return -1;
	}
	return answer;
}

console.log(digPow(89, 1)); // 1
console.log(digPow(92, 1)); // -1
console.log(digPow(46288, 3)); // 51
