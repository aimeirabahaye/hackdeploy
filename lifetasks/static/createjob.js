function toggleVisibility(id) {
    var element = document.getElementById(id)
    if (element.classList.contains('hidden')) {
        element.classList.remove('hidden');
    } else {
      element.classList.add('hidden');
    }
  }

  function selectCategory(category){
   var categoryInput = document.getElementById("selected-category");
   var categoryText = document.getElementById("category-text");
   categoryText.innerText = category;
   categoryInput.value = 'HK';
   toggleVisibility('category-select-modal');
  }