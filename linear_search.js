const linearSearch = (arr, target) => {
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] === target){
            return i;
        } 
    }
    return -1;
}


const arr = [2, 4, 90, 18, 22, 6, 110, 5, 3, 4]

const position = linearSearch(arr, 90);
if(position === -1){
    console.log("Target value not found in list");
}else{
    console.log(`Target found at position : ${position+1}`)
}
