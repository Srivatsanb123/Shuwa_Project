var logoutBtn = document.querySelector('.Logout');

logoutBtn.addEventListener('click', function() {
  var confirmLogout = confirm('Are you sure you want to logout?');
  
if (confirmLogout) {
    window.location.href = './logout';    
    console.log('User has logged out.');
  }
});
