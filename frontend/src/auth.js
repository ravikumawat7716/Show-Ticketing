export function getUserRole() {
    let token = localStorage.getItem("Auth-Token");
    if (token) {
      let userRole = localStorage.getItem("user-role");
      let Role = JSON.parse(userRole || null); // Parse to an object, default to null
      let role = null;
  
      if (Role === "USER") {
        role = 'User';
      } else if (Role === "ADMIN") {
        role = 'Admin';
      }
  
      return role; // Return the role if it's found
    }
  
    return null; // Return null if there's no token
  }
  