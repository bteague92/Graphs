// Add up and print the sum of the all of the minimum elements of each inner array:
// [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
// The expected output is given by:
// 4 + -1 + 9 + -56 + 201 + 18 = 175

const array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]];


const getSmallestSum = (arr) => {
    let smalls = [];
    let total = 0;

    // Get smallest number in array
    const getSmallest = (array) => {
        return Math.min.apply(Math, array);
    };

    // map though given arrays
    arr.map(i => {
        //push smallest value in array to smalls array
        smalls.push(getSmallest(i))
    })

    // map through smalls array
    smalls.map(i => {
        // increment total by value in array
        total += i
    })

    /// console.log the total
    console.log(total)
}

getSmallestSum(array);
