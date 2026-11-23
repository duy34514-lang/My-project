// Chuyển đổi giữa 2 mockup Đăng Nhập và Đăng Ký
const loginCard = document.getElementById("loginCard");
const registerCard = document.getElementById("registerCard");

document.getElementById("toRegister").addEventListener("click", (e) => {
  e.preventDefault();
  loginCard.classList.remove("active");
  registerCard.classList.add("active");
});

document.getElementById("toLogin").addEventListener("click", (e) => {
  e.preventDefault();
  registerCard.classList.remove("active");
  loginCard.classList.add("active");
});

document.querySelectorAll(".toggle-password").forEach((btn) => {
  btn.addEventListener("click", () => {
    const input = btn.closest(".input-group").querySelector("input");
    const isPass = input.type === "password";
    input.type = isPass ? "text" : "password";
    btn.classList.toggle("active", isPass);
  });
});
