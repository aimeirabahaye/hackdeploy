function search(){
    var userInput = document.getElementsByClassName("searchbar")[0].value;
    var reference = document.getElementById("searchref");
    reference.href ="search/" + userInput.toLowerCase();
    reference.click(); 
}