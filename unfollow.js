var items = document.getElementsByClassName('subed-btn');
for (let index = items.length - 1; index > items.length - 100; index--) {
    items[index].click();
}

var arr = document.getElementsByClassName('subed-btn');
for (let index = 0; index < arr.length; index++) {
    arr[index].click();
}
