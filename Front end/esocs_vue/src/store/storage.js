export const storage = {
    set(key, value) {
        localStorage.setItem(key, value);
    },
    get(key) {
        const value = localStorage.getItem(key);
        return value ? JSON.parse(value) : undefined;
    },
    remove(key) {
        localStorage.removeItem(key);
    }
};