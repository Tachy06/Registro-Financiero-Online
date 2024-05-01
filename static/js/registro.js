var maxSelections = 1;
var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    
for (var i = 0; i < checkboxes.length; i++) {
    checkboxes[i].addEventListener('click', function () {
        var checkedCount = document.querySelectorAll('input[type="checkbox"]:checked').length;
            
        if (checkedCount > maxSelections) {
            this.checked = false;
        }
    });
}