# Digital Alchemist - Library of Transmutations
# Format: (Element_A, Element_B): (Result, Innovation, Degradation, Lore)

RECIPES = {
    # BASIC MATERIALS
    ("sand", "fire"): ("Glass", 5, 2, "Silicon transformed by heat."),
    ("metal", "fire"): ("Liquid Metal", 5, 5, "Melted ore ready for casting."),
    ("water", "fire"): ("Steam", 5, 1, "The first step toward industrial power."),
    ("sand", "water"): ("Clay", 5, 0, "A malleable earth for building."),
    
    # ENERGY & POWER
    ("electricity", "metal"): ("Copper Wire", 10, 2, "A path for the lightning."),
    ("petroleum", "fire"): ("Combustion", 15, 20, "Explosive energy released."),
    ("sunlight", "vacuum"): ("Radiation", 10, 10, "Raw cosmic energy."),
    ("electricity", "water"): ("Hydrogen", 15, 5, "Splitting the very atoms of life."),
    
    # COMPUTATION & LOGIC
    ("logic", "electricity"): ("Binary", 20, 0, "The language of ones and zeros."),
    ("sand", "electricity"): ("Silicon Chip", 25, 5, "Modern alchemy carved into sand."),
    ("logic", "metal"): ("Mechanism", 15, 2, "Clocks, gears, and automated movement."),
    ("vacuum", "electricity"): ("Vacuum Tube", 15, 3, "An early vessel for digital thoughts."),
    
    # BIOLOGICAL & ORGANIC
    ("dna", "sunlight"): ("Photosynthesis", 20, -5, "Life learning to eat light."),
    ("dna", "water"): ("Plankton", 10, -2, "The soup of existence."),
    ("petroleum", "logic"): ("Plastic", 10, 15, "Synthetic material that never dies."),
    ("dna", "electricity"): ("Mutation", 20, 25, "Rapid, unstable biological change."),
    
    # PLANETARY & SPACE
    ("vacuum", "sand"): ("Dust Cloud", 5, 0, "The beginning of a nebula."),
    ("sunlight", "water"): ("Algae", 10, -5, "Green growth in the shallows."),
    ("metal", "logic"): ("Automaton", 30, 10, "A machine that follows orders."),
}
    # --- TIER 1: THE INDUSTRIAL SPARK ---
    ("metal", "fire"): ("Steam_Engine", 10, 15, "The heart of early industry."),
    ("steam_engine", "metal"): ("Locomotive", 12, 12, "Connecting distant lands via rail."),
    ("petroleum", "fire"): ("Combustion", 15, 20, "High-energy release for transport."),
    ("combustion", "metal"): ("Automobile", 20, 25, "Mass personal mobility."),
    ("electricity", "metal"): ("Wire", 5, 1, "The infrastructure of power."),
    ("wire", "electricity"): ("Telegraph", 15, 2, "Instant communication over distance."),
    ("sand", "fire"): ("Glass", 8, 5, "Transparent material for lenses and bulbs."),
    ("glass", "wire"): ("Lightbulb", 18, 5, "Conquering the darkness."),
    ("coal", "metal"): ("Steel", 15, 18, "The backbone of the modern skyline."),
    ("steel", "steam_engine"): ("Steamship", 20, 15, "Mastery over the oceans."),
    ("metal", "water"): ("Hydro_Turbine", 15, 2, "Harnessing the flow of rivers."),
    ("hydro_turbine", "wire"): ("Hydroelectricity", 25, 5, "Renewable power from water."),

    # --- TIER 2: THE DIGITAL AGE ---
    ("sand", "electricity"): ("Silicon", 15, 5, "The foundation of the digital world."),
    ("silicon", "logic"): ("Transistor", 25, 2, "The fundamental switch of computing."),
    ("transistor", "wire"): ("Microchip", 30, 8, "Miniaturized complexity."),
    ("microchip", "electricity"): ("Computer", 35, 10, "A machine that processes information."),
    ("computer", "wire"): ("Network", 40, 5, "Interconnected nodes."),
    ("network", "computer"): ("Internet", 50, 15, "The global information superhighway."),
    ("logic", "computer"): ("Software", 30, 0, "Instructional data for hardware."),
    ("glass", "electricity"): ("Vacuum_Tube", 20, 10, "Early electronic amplification."),
    ("software", "internet"): ("Cloud_Computing", 45, 20, "Decentralized data storage."),
    ("microchip", "glass"): ("Screen", 25, 12, "The window into the digital soul."),
    ("logic", "wire"): ("Signal", 10, 0, "Information encoded in pulse."),
    ("signal", "glass"): ("Fiber_Optics", 40, 2, "Data moving at the speed of light."),

    # --- TIER 3: AEROSPACE & TELECOM ---
    ("vacuum", "metal"): ("Vacuum_Chamber", 15, 5, "Controlled environment for testing."),
    ("combustion", "vacuum"): ("Propulsion", 40, 30, "Thrust in the void."),
    ("propulsion", "steel"): ("Rocket", 55, 40, "Escaping Earth's gravity."),
    ("rocket", "computer"): ("Satellite", 60, 25, "Eyes in the sky."),
    ("satellite", "internet"): ("GPS", 50, 5, "Global positioning and navigation."),
    ("satellite", "glass"): ("Space_Telescope", 65, 10, "Peering into the deep past."),
    ("rocket", "vacuum"): ("Space_Station", 70, 35, "A permanent human presence in orbit."),
    ("propulsion", "logic"): ("Guidance_System", 40, 10, "Precision movement through space."),
    ("steel", "aluminum"): ("Aircraft", 45, 35, "Conquering the skies."),
    ("aircraft", "petroleum"): ("Global_Travel", 50, 50, "The world becomes a village."),
    ("satellite", "logic"): ("Remote_Sensing", 55, 0, "Monitoring the Earth's health."),

    # --- TIER 4: BIOTECH & HUMAN ELEMENT ---
    ("logic", "dna"): ("Bioinformatics", 50, 5, "Mapping the code of life."),
    ("bioinformatics", "dna"): ("CRISPR", 65, 15, "Genetic editing tools."),
    ("microchip", "dna"): ("Neural_Link", 70, 25, "Direct brain-computer connection."),
    ("neural_link", "logic"): ("Artificial_Consciousness", 90, 40, "A mind without a body."),
    ("dna", "electricity"): ("Electrophoresis", 30, 5, "Analyzing genetic material."),
    ("bioinformatics", "software"): ("Vaccine_Synthesis", 60, -20, "Rapid response to pathogens."),
    ("neural_link", "software"): ("Virtual_Reality", 45, 10, "Digital worlds for the mind."),
    ("microchip", "metal"): ("Robotics", 50, 15, "Programmable mechanical labor."),
    ("robotics", "dna"): ("Cyborg", 80, 30, "The blurring of biology and machine."),
    ("logic", "biology"): ("Biomimicry", 40, -10, "Nature-inspired engineering."),

    # --- TIER 5: ENERGY REVOLUTION ---
    ("sunlight", "silicon"): ("Solar_Panel", 40, 5, "Capturing photons for power."),
    ("solar_panel", "wire"): ("Solar_Farm", 50, 10, "Large scale clean energy."),
    ("logic", "electricity"): ("Algorithm", 20, 0, "Mathematical steps for solving problems."),
    ("algorithm", "software"): ("AI", 60, 20, "Intelligence exhibited by machines."),
    ("ai", "solar_farm"): ("Smart_Grid", 70, -20, "Optimized energy distribution."),
    ("uranium", "logic"): ("Nuclear_Fission", 80, 40, "Splitting the atom."),
    ("nuclear_fission", "steam_engine"): ("Nuclear_Reactor", 85, 30, "Carbon-free, high-risk power."),
    ("sunlight", "vacuum"): ("Solar_Sail", 75, 5, "Propulsion via light pressure."),
    ("hydroelectricity", "solar_farm"): ("Renewable_Mix", 60, -30, "Diversified clean energy."),

    # --- TIER 6: CONSEQUENCES (Negative Elements) ---
    ("automobile", "petroleum"): ("Greenhouse_Gas", 0, 50, "Atmospheric warming."),
    ("greenhouse_gas", "water"): ("Ocean_Acidification", 0, 60, "Lowering the pH of the seas."),
    ("computer", "metal"): ("E-Waste", 0, 45, "Discarded electronic circuitry."),
    ("plastic", "water"): ("Microplastics", 0, 55, "Tiny particles infiltrating the food chain."),
    ("satellite", "rocket"): ("Space_Debris", 0, 40, "Orbital junk threatening launches."),
    ("ai", "internet"): ("Deepfake", 0, 35, "Synthetic media for misinformation."),
    ("internet", "logic"): ("Privacy_Erosion", 0, 40, "The loss of the personal sphere."),
    ("petroleum", "sand"): ("Oil_Spill", 0, 70, "Environmental disaster in the soil/sea."),
    ("nuclear_fission", "metal"): ("Radioactive_Waste", 0, 80, "Dangerous byproducts for millennia."),
    ("ai", "network"): ("Cyber_Warfare", 0, 60, "Digital conflict on a global scale."),

    # --- TIER 7: THE HEALERS (Remediation) ---
    ("ai", "greenhouse_gas"): ("Carbon_Capture", 50, -60, "Technological CO2 removal."),
    ("robotics", "e-waste"): ("Automated_Recycling", 45, -50, "Machines reclaiming materials."),
    ("bioinformatics", "microplastics"): ("Plastic_Eating_Bacteria", 60, -70, "Biological solution to pollution."),
    ("smart_grid", "greenhouse_gas"): ("Emission_Reduction", 55, -40, "Efficiency mitigating impact."),
    ("ethics", "ai"): ("Alignment", 70, -30, "Ensuring AI serves humanity."),
    ("ethics", "internet"): ("Digital_Rights", 50, -40, "Protecting users in the cloud."),
    ("logic", "oil_spill"): ("Bioremediation", 40, -50, "Using life to clean chemistry."),
    ("satellite", "space_debris"): ("Orbital_Sweeper", 60, -40, "Clearing the path to the stars."),

    # --- TIER 8: FUTURE SPECULATION ---
    ("logic", "vacuum"): ("Quantum_Computing", 90, 15, "Computing with subatomic states."),
    ("quantum_computing", "ai"): ("Superintelligence", 150, 50, "Intelligence beyond human grasp."),
    ("superintelligence", "ethics"): ("Singularity", 200, -100, "The point of no return for progress."),
    ("nuclear_fission", "sunlight"): ("Nuclear_Fusion", 120, 5, "The power of the stars on Earth."),
    ("robotics", "vacuum"): ("Asteroid_Mining", 100, 20, "Sourcing metals from space."),
    ("asteroid_mining", "steel"): ("Space_Elevator", 110, 25, "Affordable access to orbit."),
    ("nanotube", "metal"): ("Superalloy", 80, 5, "Ultra-strong materials."),
    ("superalloy", "space_elevator"): ("Interplanetary_Travel", 130, 30, "Humans becoming a multi-planet species."),
    ("dna", "silicon"): ("Synthetic_Biology", 85, 20, "Redesigning organisms for utility."),
    ("synthetic_biology", "carbon_capture"): ("Terraforming", 140, -80, "Making other worlds habitable."),

    # --- FINAL SYNTHESIS ---
    ("terraforming", "singularity"): ("Galactic_Civilization", 500, -500, "The ultimate expansion."),
    ("ethics", "planetary_management"): ("The_Emerald_Planet", 300, -300, "Total harmony of tech and nature."),
}

# Base elements that can't be created but are used for starting
STARTING_ELEMENTS = {"electricity", "metal", "logic", "vacuum", "sand", "petroleum", "fire", "water", "dna", "sunlight", "uranium", "coal", "ethics"}

