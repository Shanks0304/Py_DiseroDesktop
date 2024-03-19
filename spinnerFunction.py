import random
import math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Particle:
    def __init__(self, center, angle, distance, velocity_magnitude, size, alpha):
        self.velocity = QPointF(math.cos(angle) * velocity_magnitude, math.sin(angle) * velocity_magnitude)
        self.position = center + self.velocity * distance
        self.size = size
        self.alpha = alpha

    def move(self):
        self.position += self.velocity
        self.alpha -= 5  # Gradually decrease alpha to fade out particles
        self.velocity *= 0.8  # Decelerate

class Spin(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.particles = []
        self.initUI()
        self.phrases = [
            "Calibrating quantum entanglement parameters.",
            "Tuning the photon oscillation wavelengths.",
            "Aligning the cybernetic neural network.",
            "Charging the anti-gravity propulsion units.",
            "Decrypting the time-space continuum algorithms.",
            "Optimizing the holographic matrix field.",
            "Refactoring the interdimensional data streams.",
            "Synthesizing the universal solvent compounds.",
            "Energizing the plasma conduit relays.",
            "Bootstrapping the tachyon particle accelerator.",
            "Refreshing the astral projection buffers.",
            "Stabilizing the zero-point energy field.",
            "Harmonizing the subspace frequency modulators.",
            "Uploading the telepathic interface protocols.",
            "Realigning the cosmic radiation shields.",
            "Compiling the galactic positioning scripts.",
            "Initializing the quantum computing cores.",
            "Activating the chrono-synclastic infundibula.",
            "Regenerating the virtual reality landscapes.",
            "Lubricating the robotic limb actuators.",
            "Adjusting the anti-matter injection rates.",
            "Scanning for temporal anomalies.",
            "Updating the alien communication codecs.",
            "Enhancing the telekinetic power converters.",
            "Debugging the interstellar navigation system.",
            "Configuring the psychic energy detectors.",
            "Testing the wormhole stabilization matrix.",
            "Expanding the digital consciousness framework.",
            "Triangulating the multiverse coordinates.",
            "Inverting the polarity of the neutron flow.",
            "Synchronizing the orbital phase inverters.",
            "Infusing the AI with quantum entangled emotions.",
            "Deploying the nano-bot repair swarms.",
            "Cultivating the cybernetic brain farms.",
            "Fortifying the dimensional breach barricades.",
            "Programming the reality distortion fields.",
            "Refining the dark matter extraction process.",
            "Emulating the universal translator dialects.",
            "Validating the anti-gravity espresso machine.",
            "Caching the future predictive algorithms.",
            "Replenishing the photon torpedo reserves.",
            "Overclocking the telepresence avatar projectors.",
            "Building the cosmic ray deflector shields.",
            "Merging with the omnipresent AI consciousness.",
            "Calibrating the mood-enhancing lighting systems.",
            "Encrypting the intertemporal communication links.",
            "Harvesting the asteroid belt mineral resources.",
            "Initiating the singularity event horizon.",
            "Preparing the virtual quantum superposition.",
            "Balancing the universal scale of improbability.",

            "Reinitializing the sub-ether network protocols.",
            "Balancing the virtual particle accelerators.",
            "Upgrading the chrono-spatial navigation systems.",
            "Realigning the dimensional phase variators.",
            "Synchronizing the biometric encryption algorithms.",
            "Stabilizing the nano-quartz oscillation circuits.",
            "Integrating the zero-latency holographic interfaces.",
            "Enhancing the quantum flux stabilization nodes.",
            "Adjusting the spectral anomaly detection lenses.",
            "Modulating the anti-phasic energy fields.",
            "Calibrating the multi-dimensional resonance chambers.",
            "Activating the temporal flux simulation engines.",
            "Optimizing the photon-based neural synapses.",
            "Updating the astral navigation projection systems.",
            "Strengthening the quantum entanglement transceivers.",
            "Refining the galactic positional data arrays.",
            "Tuning the subatomic coherence amplifiers.",
            "Expanding the electro-plasma infusion coils.",
            "Calibrating the intergalactic communication beams.",
            "Enhancing the cognitive interface bandwidth.",
            "Rebooting the universal data compilation cores.",
            "Stabilizing the warp field containment grid.",
            "Harmonizing the syntactic translation matrices.",
            "Infusing the AI cores with quantum cognition protocols.",
            "Optimizing the graviton displacement meters.",
            "Calibrating the psychotronic wave generators.",
            "Adjusting the dark energy calibration scopes.",
            "Synthesizing adaptive metaphasic shielding layers.",
            "Integrating the subspace anomaly mapping tools.",
            "Reinforcing the time-dilation feedback loops.",
            "Upgrading the electrostatic dust repulsion system.",
            "Modulating the cosmic radiation filtration units.",
            "Enhancing the neural net mimicry algorithms.",
            "Refactoring the spatial distortion compensators.",
            "Optimizing the telekinetic energy distribution networks.",
            "Calibrating the molecular cohesion inducers.",
            "Tuning the interstellar quantum communicators.",
            "Enhancing the phase-shift teleportation arrays.",
            "Stabilizing the ion storm prediction models.",
            "Integrating the nano-fabrication molecular assemblers.",
            "Adjusting the virtual reality immersion fields.",
            "Optimizing the cybernetic empathy circuits.",
            "Calibrating the hyper-accelerated particle detectors.",
            "Enhancing the deep space telemetry probes.",
            "Refining the holographic display resolution enhancers.",
            "Tuning the anti-matter containment field regulators.",
            "Upgrading the celestial body tracking algorithms.",
            "Stabilizing the quantum computing matrix arrays.",
            "Integrating the astral energy conversion systems.",
            "Calibrating the interdimensional vortex stabilizers."
        ]
        random.shuffle(self.phrases)  # Shuffle the list of phrases
        self.current_phrase_index = 0
        self.initPhrasesTimer()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Futuristic Particle Animation')
        self.show()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)  # Refresh every 30 milliseconds

    def initPhrasesTimer(self):
        self.phrases_timer = QTimer(self)
        self.phrases_timer.timeout.connect(self.updatePhrase)
        self.phrases_timer.start(5000)  # Change phrase every 5 seconds

    def updatePhrase(self):
        self.current_phrase_index = (self.current_phrase_index + 1) % len(self.phrases)
        self.update()

    def add_particle(self):
        center = QPointF(self.width() / 2, self.height() / 2)
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(1, 10)
        velocity_magnitude = random.uniform(20, 20)  # Consistent high initial speed
        size = random.uniform(1, 3)
        alpha = random.randint(100, 200)  # Start with partial opacity
        self.particles.append(Particle(center, angle, distance, velocity_magnitude, size, alpha))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(30, 30, 30))  # Dark background
        painter.setRenderHint(QPainter.Antialiasing)

        for particle in self.particles:
            color = QColor(107, 95, 182, particle.alpha)
            painter.setPen(QPen(color, 0))
            painter.setBrush(color)
            painter.drawEllipse(particle.position, particle.size, particle.size)

        # Draw the current phrase
        painter.setFont(QFont('Arial', 14))
        painter.setPen(QColor(220, 220, 220))  # Very light grey color
        painter.drawText(self.rect(), Qt.AlignCenter, self.phrases[self.current_phrase_index])

    def animate(self):
        if len(self.particles) < 500:  # Maintain up to 500 particles at a time
            self.add_particle()

        for particle in self.particles:
            particle.move()
            if particle.alpha <= 0:
                self.particles.remove(particle)
        self.update()  # Refresh the widget