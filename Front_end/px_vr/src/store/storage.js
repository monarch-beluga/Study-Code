export const storage = {
    set(key, value) {
        localStorage.setItem(key, value);
    },
    get(key) {
        const value = localStorage.getItem(key);
        return value ? value : undefined;
    },
    remove(key) {
        localStorage.removeItem(key);
    }
};