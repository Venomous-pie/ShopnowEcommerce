export function logout() {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    localStorage.removeItem('isAuthenticated');
    window.location.href = '/login'
}