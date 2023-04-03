Repeat Header (JQuery)


var xhr = new XMLHttpRequest();
xhr.open('GET', 'header.html', true);
xhr.onreadystatechange = function() {
    if (this.readyState !== 4) return;
    if (this.status !== 200) return; // or whatever error status handling you want
    document.getElementById('header').innerHTML = this.responseText;
};
xhr.send();


