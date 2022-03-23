const hamburger = document.querySelector("#hamburger");
const menuHamburger = document.querySelector("#hamburger-menu");

hamburger.addEventListener("click", () => {
  if (menuHamburger.classList.contains("hidden")) {
    menuHamburger.classList.remove("hidden");
    menuHamburger.classList.add("flex");
    setTimeout(() => {
      menuHamburger.classList.remove("opacity-0");
      menuHamburger.classList.add("opacity-85");
    }, 0);
  } else {
    menuHamburger.classList.remove("opacity-85");
    menuHamburger.classList.add("opacity-0");
    setTimeout(() => {
      menuHamburger.classList.remove("flex");
      menuHamburger.classList.add("hidden");
    }, 200);
  }
});
