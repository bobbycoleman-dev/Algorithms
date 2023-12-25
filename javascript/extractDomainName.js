url1 = "http://github.com/carbonfive/raygun"; // -> domain name = "github"
url2 = "http://www.zombie-bites.com"; // -> domain name = "zombie-bites"
url3 = "https://www.cnet.com"; // -> domain name = cnet"
url4 = "www.cnet.com"; // -> domain name = cnet"
url5 = "bobby.com"; // -> domain name = cnet"

function domainName(url) {
	let result = "";
	const re = /https|http|www/gi;

	if (url.includes("https://")) url = url.replace("https://", "www.");
	if (url.includes("http://")) url = url.replace("http://", "www.");
	if (url.includes("www.")) url = url.replace("www.", "");
	if (!url.includes("www")) url = `www.${url}`;

	console.log(url);
	for (let i = 0; i < url.length; i++) {
		if (url[i] == ".") {
			for (let j = i + 1; j < url.length; j++) {
				result += url[j];
				if (url[j + 1] == ".") return result;
			}
		}
	}
}

console.log(domainName(url1));
console.log(domainName(url2));
console.log(domainName(url3));
console.log(domainName(url4));
console.log(domainName(url5));
