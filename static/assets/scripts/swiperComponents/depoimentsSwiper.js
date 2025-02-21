let swiper = new Swiper(".depoimentsSwiper", {
  loop: true,
  cssMode: true,
  autoplay: {
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  pagination: {
    el: ".swiper-pagination",
  },
  mousewheel: true,
  keyboard: true,
});
