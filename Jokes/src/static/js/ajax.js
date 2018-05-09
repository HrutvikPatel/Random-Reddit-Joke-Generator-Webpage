$("#random").click(function(e) {
    e.preventDefault();
    getData();
})

function getData() {
    $.get("Twitter-Jokes", function(data, status){
        $("#author").text(data["author"])
        $("#q").text(data["q"])
        $("#a").text(data["a"])
    });
}

$(document).ready(function() {
    getData();
})