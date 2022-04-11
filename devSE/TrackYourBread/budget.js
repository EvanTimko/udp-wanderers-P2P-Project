const n = new Date();
const y = n.getFullYear();
const m = n.getMonth();
const monthArr = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const month = monthArr[m];
document.getElementById("date").innerHTML = month + ' ' + y;

// Get the modal
var modal = document.getElementById('id012');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}