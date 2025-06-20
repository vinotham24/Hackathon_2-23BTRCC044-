from PIL import Image

def predict_disease(image: Image.Image, report: str) -> str:
    report = report.lower()

    # 🫁 LUNG CONDITIONS
    if "pneumonia" in report:
        return "🫁 Pneumonia Detected"
    elif "pulmonary edema" in report or "fluid in lungs" in report:
        return "💧 Pulmonary Edema"
    elif "atelectasis" in report:
        return "🫁 Lung Collapse (Atelectasis)"
    elif "pleural effusion" in report:
        return "💧 Pleural Effusion (Fluid near lungs)"
    elif "tuberculosis" in report or "tb" in report:
        return "🧫 Pulmonary Tuberculosis"
    elif "copd" in report or "chronic obstructive" in report:
        return "🌬️ COPD (Chronic Obstructive Pulmonary Disease)"
    elif "lung mass" in report or "lung tumor" in report:
        return "🎯 Suspicious Lung Tumor"
    elif "bronchitis" in report:
        return "🔥 Bronchitis (Airway Inflammation)"

    # 🧠 BRAIN CONDITIONS
    elif "stroke" in report or "ischemic" in report:
        return "🧠 Stroke (Ischemic)"
    elif "hemorrhage" in report or "bleeding" in report:
        return "🩸 Brain Hemorrhage"
    elif "brain tumor" in report:
        return "🎯 Brain Tumor Detected"
    elif "brain swelling" in report or "edema" in report:
        return "💧 Brain Edema (Swelling)"
    elif "aneurysm" in report:
        return "⚠️ Brain Aneurysm"
    elif "hydrocephalus" in report:
        return "🧠 Hydrocephalus (CSF buildup)"
    elif "meningitis" in report:
        return "🦠 Meningitis (Brain Infection)"
    elif "seizure" in report:
        return "⚡ Possible Seizure Activity"

    # ❤️ HEART CONDITIONS
    elif "cardiomegaly" in report or "enlarged heart" in report:
        return "❤️ Cardiomegaly (Enlarged Heart)"
    elif "heart failure" in report:
        return "🫀 Possible Heart Failure"
    elif "arrhythmia" in report:
        return "📉 Irregular Heartbeat (Arrhythmia)"
    elif "pericardial effusion" in report:
        return "💧 Fluid around Heart (Pericardial Effusion)"

    # 🩺 KIDNEY CONDITIONS
    elif "kidney stone" in report:
        return "🪨 Kidney Stones"
    elif "hydronephrosis" in report:
        return "💧 Kidney Swelling (Hydronephrosis)"
    elif "renal failure" in report:
        return "🚫 Kidney Failure"
    elif "cyst" in report and "kidney" in report:
        return "🌀 Kidney Cyst Detected"

    # 🦴 SPINE / BONES
    elif "fracture" in report or "break" in report:
        return "🦴 Bone Fracture"
    elif "compression" in report and "spine" in report:
        return "🔩 Spinal Compression"
    elif "scoliosis" in report:
        return "↩️ Scoliosis (Spinal Curvature)"
    elif "osteoporosis" in report:
        return "🦴 Osteoporosis (Bone Weakness)"

    # 👁️ EYE CONDITIONS
    elif "glaucoma" in report:
        return "👁️ Glaucoma Detected"
    elif "retina" in report and "detachment" in report:
        return "⚠️ Retinal Detachment"
    elif "optic nerve" in report and "damage" in report:
        return "🧠 Optic Nerve Damage"
    elif "cataract" in report:
        return "🌫️ Cataract (Lens Clouding)"

    # GENERAL OR NORMAL FINDINGS
    elif "normal" in report:
        return "✅ No Abnormal Findings"
    elif "no abnormality" in report:
        return "✅ Report Normal"
    elif "inflammation" in report:
        return "🔥 General Inflammation Detected"
    elif "opacity" in report or "shadow" in report:
        return "⚠️ Possible Shadow/Opacity in Imaging"

    # IF NOTHING MATCHES
    else:
        return "❓ Diagnosis unclear from report"
