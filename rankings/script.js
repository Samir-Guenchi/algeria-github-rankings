// Algeria GitHub Rankings - Interactive Features

// Wilayas data
const wilayas = [
    { code: "01", name_en: "Adrar", name_ar: "أدرار" },
    { code: "02", name_en: "Chlef", name_ar: "الشلف" },
    { code: "03", name_en: "Laghouat", name_ar: "الأغواط" },
    { code: "04", name_en: "Oum El Bouaghi", name_ar: "أم البواقي" },
    { code: "05", name_en: "Batna", name_ar: "باتنة" },
    { code: "06", name_en: "Béjaïa", name_ar: "بجاية" },
    { code: "07", name_en: "Biskra", name_ar: "بسكرة" },
    { code: "08", name_en: "Béchar", name_ar: "بشار" },
    { code: "09", name_en: "Blida", name_ar: "البليدة" },
    { code: "10", name_en: "Bouira", name_ar: "البويرة" },
    { code: "11", name_en: "Tamanrasset", name_ar: "تمنراست" },
    { code: "12", name_en: "Tébessa", name_ar: "تبسة" },
    { code: "13", name_en: "Tlemcen", name_ar: "تلمسان" },
    { code: "14", name_en: "Tiaret", name_ar: "تيارت" },
    { code: "15", name_en: "Tizi Ouzou", name_ar: "تيزي وزو" },
    { code: "16", name_en: "Algiers", name_ar: "الجزائر" },
    { code: "17", name_en: "Djelfa", name_ar: "الجلفة" },
    { code: "18", name_en: "Jijel", name_ar: "جيجل" },
    { code: "19", name_en: "Sétif", name_ar: "سطيف" },
    { code: "20", name_en: "Saïda", name_ar: "سعيدة" },
    { code: "21", name_en: "Skikda", name_ar: "سكيكدة" },
    { code: "22", name_en: "Sidi Bel Abbès", name_ar: "سيدي بلعباس" },
    { code: "23", name_en: "Annaba", name_ar: "عنابة" },
    { code: "24", name_en: "Guelma", name_ar: "قالمة" },
    { code: "25", name_en: "Constantine", name_ar: "قسنطينة" },
    { code: "26", name_en: "Médéa", name_ar: "المدية" },
    { code: "27", name_en: "Mostaganem", name_ar: "مستغانم" },
    { code: "28", name_en: "M'Sila", name_ar: "المسيلة" },
    { code: "29", name_en: "Mascara", name_ar: "معسكر" },
    { code: "30", name_en: "Ouargla", name_ar: "ورقلة" },
    { code: "31", name_en: "Oran", name_ar: "وهران" },
    { code: "32", name_en: "El Bayadh", name_ar: "البيض" },
    { code: "33", name_en: "Illizi", name_ar: "إليزي" },
    { code: "34", name_en: "Bordj Bou Arréridj", name_ar: "برج بوعريريج" },
    { code: "35", name_en: "Boumerdès", name_ar: "بومرداس" },
    { code: "36", name_en: "El Tarf", name_ar: "الطارف" },
    { code: "37", name_en: "Tindouf", name_ar: "تندوف" },
    { code: "38", name_en: "Tissemsilt", name_ar: "تيسمسيلت" },
    { code: "39", name_en: "El Oued", name_ar: "الوادي" },
    { code: "40", name_en: "Khenchela", name_ar: "خنشلة" },
    { code: "41", name_en: "Souk Ahras", name_ar: "سوق أهراس" },
    { code: "42", name_en: "Tipaza", name_ar: "تيبازة" },
    { code: "43", name_en: "Mila", name_ar: "ميلة" },
    { code: "44", name_en: "Aïn Defla", name_ar: "عين الدفلى" },
    { code: "45", name_en: "Naâma", name_ar: "النعامة" },
    { code: "46", name_en: "Aïn Témouchent", name_ar: "عين تموشنت" },
    { code: "47", name_en: "Ghardaïa", name_ar: "غرداية" },
    { code: "48", name_en: "Relizane", name_ar: "غليزان" },
    { code: "49", name_en: "Timimoun", name_ar: "تيميمون" },
    { code: "50", name_en: "Bordj Badji Mokhtar", name_ar: "برج باجي مختار" },
    { code: "51", name_en: "Ouled Djellal", name_ar: "أولاد جلال" },
    { code: "52", name_en: "Béni Abbès", name_ar: "بني عباس" },
    { code: "53", name_en: "In Salah", name_ar: "عين صالح" },
    { code: "54", name_en: "In Guezzam", name_ar: "عين قزام" },
    { code: "55", name_en: "Touggourt", name_ar: "تقرت" },
    { code: "56", name_en: "Djanet", name_ar: "جانت" },
    { code: "57", name_en: "El M'Ghair", name_ar: "المغير" },
    { code: "58", name_en: "El Meniaa", name_ar: "المنيعة" },
    { code: "59", name_en: "Aflou", name_ar: "أفلو" },
    { code: "60", name_en: "Barika", name_ar: "بريكة" },
    { code: "61", name_en: "Ksar Chellala", name_ar: "قصر الشلالة" },
    { code: "62", name_en: "Messaad", name_ar: "مسعد" },
    { code: "63", name_en: "Aïn Oussara", name_ar: "عين وسارة" },
    { code: "64", name_en: "Bou Saâda", name_ar: "بوسعادة" },
    { code: "65", name_en: "El Abiodh Sidi Cheikh", name_ar: "الأبيض سيدي الشيخ" },
    { code: "66", name_en: "El Kantara", name_ar: "القنطرة" },
    { code: "67", name_en: "Bir El Ater", name_ar: "بئر العاتر" },
    { code: "68", name_en: "Ksar El Boukhari", name_ar: "قصر البخاري" },
    { code: "69", name_en: "El Aricha", name_ar: "العريشة" }
];

// Render wilayas
function renderWilayas(wilayasToRender = wilayas) {
    const grid = document.getElementById('wilayasGrid');
    grid.innerHTML = wilayasToRender.map(wilaya => `
        <a href="by-wilaya/wilaya_${wilaya.code}.md" class="wilaya-card">
            <div class="wilaya-code">${wilaya.code}</div>
            <div class="wilaya-name">${wilaya.name_en}</div>
            <div class="wilaya-name-ar">${wilaya.name_ar}</div>
        </a>
    `).join('');
}

// Search functionality
function setupSearch() {
    const searchInput = document.getElementById('wilayaSearch');
    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const filtered = wilayas.filter(w => 
            w.name_en.toLowerCase().includes(query) ||
            w.name_ar.includes(query) ||
            w.code.includes(query)
        );
        renderWilayas(filtered);
    });
}

// Animate stats counter
function animateStats() {
    const stats = document.querySelectorAll('.stat-value');
    stats.forEach(stat => {
        const target = parseInt(stat.getAttribute('data-target') || stat.textContent);
        if (isNaN(target)) return;

        let current = 0;
        const increment = target / 50;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                stat.textContent = target.toLocaleString();
                clearInterval(timer);
            } else {
                stat.textContent = Math.floor(current).toLocaleString();
            }
        }, 30);
    });
}

// Update last update time
function updateLastUpdate() {
    const lastUpdateEl = document.getElementById('lastUpdate');
    if (lastUpdateEl) {
        const now = new Date();
        lastUpdateEl.textContent = now.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    }
}

// Smooth scroll for anchor links
function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Navbar scroll effect
function setupNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        } else {
            navbar.style.boxShadow = 'none';
        }

        lastScroll = currentScroll;
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    renderWilayas();
    setupSearch();
    animateStats();
    updateLastUpdate();
    setupSmoothScroll();
    setupNavbarScroll();
});
