import os
import sys

try:
    import qiskit
    from qiskit_aer import Aer
except ImportError:
    os.system('pip install qiskit qiskit-aer matplotlib pylatexenc ipywidgets')

import numpy as np
import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output

output_canvas = widgets.Output()

def update_simulation(change):
    theta = theta_slider.value
    phi = phi_slider.value
    
    with output_canvas:
        clear_output(wait=True)
        plt.close('all') 
        
        initial_state = Statevector([1, 0])
        c0 = np.cos(theta/2)
        c1 = np.exp(1j*phi) * np.sin(theta/2)
        user_state = Statevector([c0, c1])
        
        display(HTML(f"""
            <div style="background-color: #000000; padding: 20px; border: 2px solid #00FF00; border-radius: 8px; font-family: 'Courier New', monospace; color: #00FF00; box-shadow: 0 0 20px #00FF00; max-width: 800px;">
                <h2 style="color: #00FF00; text-shadow: 0 0 8px #00FF00; margin-top:0;">> BLOCH KÜRESİ ANALİZ SİSTEMİ</h2>
                <p style="margin: 2px 0;"><b>[DATA]: θ = {theta:.4f} | φ = {phi:.4f}</b></p>
                <hr style="border: 0.5px solid #00FF00; margin: 10px 0;">
                <p style="font-size: 13px;">
                    <span style="color: #FF0000;">● [REFERANS]:</span> |0⟩ Baseline<br>
                    <span style="color: #00FF00;">● [AKTİF]:</span> Süperpozisyon Durumu
                </p>
            </div>
        """))
        
        fig = plot_bloch_multivector([initial_state, user_state])
        fig.patch.set_facecolor('#000000')
        display(fig)
        
        display(HTML("""
            <div style="background-color: #050505; padding: 15px; color: #00cc00; font-family: 'Courier New'; border-top: 2px solid #FF0000; max-width: 800px;">
                <p><b> GÖZLEMCİ NOTU:</b> Vektör ekvator düzlemine yaklaştıkça parçacığın 
                dalga fonksiyonu genişler. Bu, verinin hem '0' hem '1' bitlerinde 
                eşzamanlı olarak işlendiği <b>Süperpozisyon</b> evresidir.</p>
            </div>
        """))

style = {'description_width': 'initial'}
theta_slider = widgets.FloatSlider(value=0, min=0, max=np.pi, step=0.02, description='[ANGLE_Θ]:', layout={'width': '500px'}, style=style)
phi_slider = widgets.FloatSlider(value=0, min=0, max=2*np.pi, step=0.02, description='[PHASE_Φ]:', layout={'width': '500px'}, style=style)

theta_slider.observe(update_simulation, names='value')
phi_slider.observe(update_simulation, names='value')

ui_elements = widgets.VBox([theta_slider, phi_slider])
display(ui_elements, output_canvas)

update_simulation(None)
