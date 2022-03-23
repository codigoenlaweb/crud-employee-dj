const prev = document.querySelector("#prev");
const next = document.querySelector("#next");
const carousel = document.querySelector("#carousel");
let countImg = 0;

prev.addEventListener("click", () => {
  console.log("prev");
  if (countImg != 0) {
    countImg--;
    carousel.style.transform = `translateX(-${25 * countImg}%)`;
  } else {
    countImg = 3;
    carousel.style.transform = `translateX(-${25 * countImg}%)`;
  }
});

next.addEventListener("click", () => {
  if (countImg != 3) {
    countImg++;
    
    setTimeout(() => {
        carousel.style.transform = `translateX(-${25 * countImg}%)`;
    }, 0);
  } else {
    countImg = 0;
    setTimeout(() => {
      carousel.style.transform = `translateX(-${25 * countImg}%)`;
    }, 0);
  }
  console.log("next");
});
