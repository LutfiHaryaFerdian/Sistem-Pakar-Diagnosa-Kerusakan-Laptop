from typing import Dict, List, Any

# ============================
#   FULL KNOWLEDGE BASE
# ============================

FAULTS: Dict[str, str] = {
    "K1": "LCD Rusak",
    "K2": "RAM Rusak",
    "K3": "HDD Rusak",
    "K4": "VGA Rusak",
    "K5": "Sound Card Rusak",
    "K6": "OS Bermasalah",
    "K7": "Aplikasi Rusak",
    "K8": "Baterai dan CMOS Bermasalah",
    "K9": "Processor Bermasalah",
    "K10": "Kekurangan Memori",
    "K11": "Kekurangan Memori VGA",
    "K12": "Clock Processor Kurang Tinggi",
    "K13": "Adapter Charger Bermasalah",
    "K14": "Kekurangan Daya Baterai",
    "K15": "Perangkat USB Rusak",
    "K16": "Keyboard Rusak",
    "K17": "Touchpad Rusak",
    "K18": "Motherboard Rusak",
    "K19": "Kabel Power Rusak",
    "K20": "Kabel Sata/IDE Rusak",
    "K21": "CD/DVD/ROM/RW Rusak",
    "K22": "BIOS Error",
}

SYMPTOMS: Dict[str, str] = {
    "G1": "Tombol hidup tapi tidak ada tampilan",
    "G2": "Garis horizontal/vertikal di monitor",
    "G3": "Tidak ada tampilan awal BIOS",
    "G4": "Pesan Error pada BIOS",
    "G5": "Alarm BIOS berbunyi",
    "G6": "Suara aneh dari HDD",
    "G7": "Sering hang/crash",
    "G8": "Selalu pindai disk saat boot",
    "G9": "Error saat menjalankan aplikasi",
    "G10": "Driver perangkat tidak terdeteksi",
    "G11": "OS restart otomatis",
    "G12": "Blue Screen (BSOD)",
    "G13": "Suara tetap keluar meski driver ok",
    "G14": "Error menjalankan aplikasi audio",
    "G15": "Error saat OS dimuat dari HDD",
    "G16": "Daya tidak tersimpan",
    "G17": "Tidak bisa connect internet",
    "G18": "Windows kekurangan virtual memory",
    "G19": "Aplikasi berjalan lambat",
    "G20": "Performa grafis sangat berat",
    "G21": "Perangkat tidak terdeteksi di BIOS",
    "G22": "Informasi salah di BIOS",
    "G23": "Peringatan baterai saat booting",
    "G24": "Input keyboard mati",
    "G25": "Pointer touchpad tidak merespon",
    "G26": "Sebagian karakter input mati",
    "G27": "Bip panjang saat laptop dinyalakan",
    "G28": "Laptop sulit dinyalakan",
    "G29": "Kabel power tergores",
    "G30": "Tidak ada indikasi daya",
    "G31": "Mati total",
    "G32": "Laptop hidup lalu layar mati",
    "G33": "Bip berulang",
    "G34": "Butuh restart OS untuk lanjut",
    "G35": "Tanggal/jam selalu reset",
    "G36": "Power nyala tapi tidak tampil",
    "G37": "CD/DVD tidak terdeteksi",
    "G38": "CD/DVD tidak bisa eject",
    "G39": "Checksum BIOS Error",
    "G40": "OS tidak muncul",
    "G41": "Tidak menyala saat tekan tombol power",
}

# Kategorisasi gejala untuk fitur filter
SYMPTOM_CATEGORIES: Dict[str, List[str]] = {
    "Hardware": ["G1", "G2", "G3", "G5", "G6", "G21", "G24", "G25", "G26", "G27", "G28", "G29", "G30", "G31", "G32", "G33", "G36", "G37", "G38", "G41"],
    "Software": ["G7", "G9", "G11", "G12", "G14", "G15", "G17", "G18", "G19", "G20", "G34", "G40"],
    "BIOS": ["G3", "G4", "G5", "G22", "G35", "G39"],
    "Power": ["G16", "G23", "G28", "G29", "G30", "G32", "G41"],
    "Display": ["G1", "G2", "G20", "G32", "G36"],
}

# ====== RULES SESUAI JURNAL ======

RULES: Dict[str, List[str]] = {
    "K1": ["G1", "G2", "G26"],
    "K2": ["G3", "G4", "G5", "G11", "G12", "G33"],
    "K3": ["G6", "G7", "G8", "G10", "G21", "G22", "G34"],
    "K4": ["G3", "G9", "G12"],
    "K5": ["G10", "G13", "G14"],
    "K6": ["G11", "G15", "G40"],
    "K7": ["G7", "G12"],
    "K8": ["G16", "G17", "G35"],
    "K9": ["G1", "G3", "G4"],
    "K10": ["G18", "G19"],
    "K11": ["G9", "G20"],
    "K12": ["G19"],
    "K13": ["G41"],
    "K14": ["G5", "G23"],
    "K15": ["G10"],
    "K16": ["G10", "G24", "G27"],
    "K17": ["G10", "G25"],
    "K18": ["G28", "G31", "G36"],
    "K19": ["G29", "G30", "G32"],
    "K20": ["G10", "G21"],
    "K21": ["G37", "G38"],
    "K22": ["G39", "G3"],
}

# ====== CF PAKAR (dari jurnal) ======

CF_PAKAR: Dict[str, float] = {
    "G1": 0.8, "G2": 0.8, "G3": 1.0, "G4": 0.8, "G5": 0.8,
    "G6": 0.6, "G7": 1.0, "G8": 0.6, "G9": 0.6, "G10": 0.8,
    "G11": 0.6, "G12": 0.8, "G13": 0.6, "G14": 0.6,
    "G15": 0.6, "G16": 0.8, "G17": 0.6, "G18": 0.6,
    "G19": 0.6, "G20": 0.6, "G21": 1.0, "G22": 1.0,
    "G23": 0.8, "G24": 0.8, "G25": 0.8, "G26": 0.6,
    "G27": 0.6, "G28": 0.8, "G29": 0.8, "G30": 0.8,
    "G31": 0.8, "G32": 0.8, "G33": 1.0, "G34": 0.6,
    "G35": 1.0, "G36": 1.0, "G37": 0.6, "G38": 0.6,
    "G39": 1.0, "G40": 0.6, "G41": 1.0,
}

CF_FALLBACK: float = 0.6
P_YES: float = 0.9
P_NO: float = 0.1


# ============================
#   NAIVE BAYES + CF ENGINE
# ============================

def naive_bayes(symptoms: List[str]) -> Dict[str, float]:
    num_faults = len(FAULTS)
    prior = 1 / num_faults
    scores: Dict[str, float] = {}

    for fault, rule_sym in RULES.items():
        score = prior
        for s in symptoms:
            score *= P_YES if s in rule_sym else P_NO
        scores[fault] = score

    total = sum(scores.values())
    for k in scores:
        scores[k] /= total

    return scores


def cf_gejala(symptom: str, intensity: float) -> float:
    return CF_PAKAR.get(symptom, CF_FALLBACK) * intensity


def combine_cf(a: float, b: float) -> float:
    return a + b * (1 - a)


def final_cf(cf_list: List[float]) -> float:
    if not cf_list:
        return 0.0
    c = cf_list[0]
    for v in cf_list[1:]:
        c = combine_cf(c, v)
    return c


def diagnose(symptoms_with_intensity: Dict[str, float]) -> Dict[str, Any] | None:
    symptoms = list(symptoms_with_intensity.keys())

    nb_scores = naive_bayes(symptoms)
    
    all_results: List[Dict[str, Any]] = []
    
    for fault_code, fault_rules in RULES.items():
        cf_list: List[float] = []
        detail: Dict[str, Any] = {}
        
        for s, intens in symptoms_with_intensity.items():
            if s in fault_rules:
                cf_val = cf_gejala(s, intens)
                cf_list.append(cf_val)
                detail[s] = {
                    "gejala": SYMPTOMS[s],
                    "cf_gejala": cf_val,
                    "intensitas": intens
                }
        
        if cf_list:
            cf_total = final_cf(cf_list)
            all_results.append({
                "fault_code": fault_code,
                "fault_name": FAULTS[fault_code],
                "cf_percent": cf_total * 100,
                "nb_score": nb_scores[fault_code],
                "details": detail
            })
    
    all_results.sort(key=lambda x: x["cf_percent"], reverse=True)
    
    top_3 = all_results[:3] if len(all_results) >= 3 else all_results
    
    top_result = top_3[0] if top_3 else None
    
    if top_result:
        return {
            "fault_code": top_result["fault_code"],
            "fault_name": top_result["fault_name"],
            "cf_percent": top_result["cf_percent"],
            "nb_all": nb_scores,
            "details": top_result["details"],
            "top_3": top_3
        }
    
    return None