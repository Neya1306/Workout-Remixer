
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

//code for slides
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("slide");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  slides[slideIndex-1].style.display = "block";  
  setTimeout(showSlides, 5000); // Change image every 5 seconds
}

// Modal functionality
// Modal functionality for workouts
const openModalWorkout = document.querySelectorAll("[data-open-modal-workout]");
const modalWorkout = document.querySelectorAll("[data-modal-workout]");
const closeModalWorkout = document.querySelectorAll("[data-close-modal-workout]");

openModalWorkout.forEach((button, index) => {
  button.addEventListener("click", () => {
    modalWorkout[index].showModal();
  });
});

closeModalWorkout.forEach((button, index) => {
  button.addEventListener("click", () => {
    modalWorkout[index].close();
  });
});

// Modal functionality for routines
const openModalRoutine = document.querySelector("[data-open-modal-routine]");
const modalRoutine = document.querySelector("[data-modal-routine]");
const closeModalRoutine = document.querySelector("[data-close-modal-routine]");

openModalRoutine.addEventListener("click", () => {
  modalRoutine.showModal();
});

closeModalRoutine.addEventListener("click", () => {
  modalRoutine.close();
});


async function main(){
    const users = await getUserData();
    loadTable(users);
    showSlides(); // Call the showSlides function
}

main();