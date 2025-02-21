let btnMenu = document.querySelector(".header__hamburger");
let headerUl = document.querySelector(".headerList");

btnMenu.addEventListener("click", (e) => {
  e.stopPropagation();

  headerUl.classList.toggle("headerList--show");
  btnMenu.classList.toggle("header__hamburger--show");
});
