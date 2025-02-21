let swiper = new Swiper(".mySwiper", {
  loop: true,
  direction: "horizontal",
  spaceBetween: 16,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true,
  breakpoints: {
    1080: {
      direction: "vertical",
    },
  },
});

let swiper2 = new Swiper(".mySwiper2", {
  loop: true,
  spaceBetween: 10,
  slidesPerView: 1,
  effect: "cube",
  grabCursor: true,
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  cubeEffect: {
    shadow: false,
    slideShadows: true,
    shadowOffset: 20,
    shadowScale: 0.94,
  },
  thumbs: {
    swiper: swiper,
  },
});
