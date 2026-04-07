function validateForm(){

let pass = document.getElementById("password").value;
let cpass = document.getElementById("confirmPassword").value;

if(pass !== cpass){
alert("Password not matched");
return false;
}

alert("Registration Successful 🎉");
return true;
}

function togglePassword(){
let p = document.getElementById("password");
p.type = p.type === "password" ? "text" : "password";
}

function checkStrength(){

let pass = document.getElementById("password").value;
let bar = document.getElementById("strength");

if(pass.length < 4){
bar.style.background="red";
bar.style.width="30%";
}
else if(pass.length < 8){
bar.style.background="orange";
bar.style.width="60%";
}
else{
bar.style.background="lime";
bar.style.width="100%";
}

}