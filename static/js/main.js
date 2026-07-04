document.addEventListener('DOMContentLoaded', () => {
    // Simple script to handle select focus state visualization
    const selects = document.querySelectorAll('select');
    selects.forEach(select => {
        select.addEventListener('focus', (e) => {
            if(e.target.previousElementSibling) e.target.previousElementSibling.classList.add('text-secondary');
        });
        select.addEventListener('blur', (e) => {
            if(e.target.previousElementSibling) e.target.previousElementSibling.classList.remove('text-secondary');
        });
    });

    // Mobile menu toggle
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('open');
        });
    }

    // Save This Look Feature
    const saveBtn = document.getElementById('save-look-btn');
    const savedBadge = document.getElementById('saved-badge');
    const clearSaved = document.getElementById('clear-saved-looks');
    const STORAGE_KEY = 'lara_saved_looks';

    const getSavedLooks = () => JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
    const setSavedLooks = (looks) => localStorage.setItem(STORAGE_KEY, JSON.stringify(looks));

    const mobileClearSaved = document.getElementById('mobile-clear-saved');

    const updateBadge = () => {
        const looks = getSavedLooks();
        if (savedBadge) {
            if (looks.length > 0) {
                savedBadge.textContent = looks.length;
                savedBadge.classList.remove('hidden');
                if (mobileClearSaved) mobileClearSaved.classList.remove('hidden');
            } else {
                savedBadge.classList.add('hidden');
                if (mobileClearSaved) mobileClearSaved.classList.add('hidden');
            }
        }
    };

    const showToast = (message) => {
        const toast = document.createElement('div');
        toast.className = 'fixed bottom-4 left-1/2 transform -translate-x-1/2 bg-inverse-surface text-inverse-on-surface px-4 py-2 rounded-lg shadow-lg text-label-md z-50 animate-fade-in-up';
        toast.textContent = message;
        document.body.appendChild(toast);
        setTimeout(() => {
            toast.classList.add('opacity-0', 'transition-opacity');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    };

    if (saveBtn) {
        try {
            const style = saveBtn.dataset.style;
            const products = JSON.parse(saveBtn.dataset.products || '[]');
            const lookKey = btoa(style + products.join('-')).substring(0, 20); // Unique key
            
            const looks = getSavedLooks();
            const isSaved = looks.some(l => l.key === lookKey);

            if (isSaved) {
                document.getElementById('save-icon').textContent = 'bookmark_added';
                document.getElementById('save-text').textContent = 'Saved ✓';
            }

            saveBtn.addEventListener('click', () => {
                const currentLooks = getSavedLooks();
                if (!currentLooks.some(l => l.key === lookKey)) {
                    currentLooks.push({
                        key: lookKey,
                        style: style,
                        products: products,
                        palette: JSON.parse(saveBtn.dataset.palette || '[]'),
                        price: saveBtn.dataset.price,
                        date: new Date().toISOString()
                    });
                    setSavedLooks(currentLooks);
                    
                    document.getElementById('save-icon').textContent = 'bookmark_added';
                    document.getElementById('save-text').textContent = 'Saved ✓';
                    showToast('Look saved to this browser.');
                    updateBadge();
                }
            });
        } catch (e) {
            console.error('Error parsing save data:', e);
        }
    }

    const handleClear = (e) => {
        e.preventDefault();
        localStorage.removeItem(STORAGE_KEY);
        updateBadge();
        showToast('Saved looks cleared.');
        if (saveBtn) {
            document.getElementById('save-icon').textContent = 'bookmark';
            document.getElementById('save-text').textContent = 'Save This Look';
        }
    };

    if (clearSaved) clearSaved.addEventListener('click', handleClear);
    if (mobileClearSaved) mobileClearSaved.addEventListener('click', handleClear);

    // Initial badge update
    updateBadge();

    // Form submission loading state
    const form = document.getElementById('recommendation-form');
    const submitBtn = document.getElementById('submit-btn');
    const submitText = document.getElementById('submit-text');

    if (form && submitBtn && submitText) {
        form.addEventListener('submit', () => {
            submitBtn.disabled = true;
            submitText.innerHTML = '<span class="material-symbols-outlined animate-spin" style="font-size: 18px;">sync</span> LARA is curating your perfect look...';
        });
    }
});
