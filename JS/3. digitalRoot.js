function digital_root(n) {
	let sum = 0;
	let x = n % 9;
	if (n === 0) {
		return sum = 0
	} else {
		switch (x) {
			case 0:
				return sum = 9;
				break
			default: 
				return sum = x; 
		};
	};
};

console.log(digital_root(456));