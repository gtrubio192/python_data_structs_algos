
const merge_sort = (left, right) => {
    let sorted_arr = [];
    let r_index = 0;
    let l_index = 0;

    // run though our arrays and compare
    while(l_index < left.length && r_index < right.length) {
        if(left[l_index] < right[r_index]) {
            sorted_arr.push(left[l_index]);
            l_index += 1;
        }
        else {
            sorted_arr.push(right[r_index]);
            r_index += 1;
        }
    }
    return sorted_arr.concat(left.slice(l_index), right.slice(r_index))
}

const divide_array = (arr) => {
    if(arr.length <= 1) {
        return arr;
    }
    let middle = Math.floor(arr.length/2);
    const left = divide_array(arr.slice(0, middle));
    const right = divide_array(arr.slice(middle));

    return merge_sort(left, right);
}


let arr = [5,33,24, 7,2, 787, 999, 6]
console.log(divide_array(arr));
