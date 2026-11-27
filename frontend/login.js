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

document.querySelector("form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email_address").value.trim();
  const password = document.getElementById("password").value;

  try {
    const res = await fetch("http://127.0.0.1:8000/api/auth/login", {
      method: "post",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    const data = await res.json();

    if (!res.ok) {
      alert(data.detail || "đăng nhập thất bại");
      return;
    }

    localStorage.setItem("access_token", data.access_token);
    alert("đăng nhập thành công");
  } catch (err) {
    console.error(err);
    alert("không thể kết nối tới backend");
  }
});
