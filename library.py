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
    
    # --- TIER 1: THE INDUSTRIAL SPARK (EXPANDED) ---
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
    
    # NEW INDUSTRIAL LATERALS (The "Connectors")
    ("coal", "fire"): ("Coke", 5, 10, "Purified fuel for high-heat smelting."),
    ("coke", "metal"): ("Cast_Iron", 10, 12, "Brittle but vital early structural metal."),
    ("petroleum", "water"): ("Oil_Slick", 0, 30, "A sign of industrial leakage."),
    ("sand", "metal"): ("Foundry", 10, 15, "The place where civilization is cast."),
    ("clay", "fire"): ("Ceramic", 8, 2, "Heat-resistant material for engines."),
    ("clay", "electricity"): ("Aluminum", 25, 15, "Lightweight metal extracted via electrolysis."),
    ("petroleum", "fire"): ("Kerosene", 12, 18, "A stable liquid fuel for lamps and jets."),

    # --- TIER 2: THE DIGITAL AGE (EXPANDED) ---
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
    
    # NEW DIGITAL LATERALS (The "Complexity" layer)
    ("software", "logic"): ("Algorithm", 25, 0, "Mathematical steps for solving problems."),
    ("algorithm", "logic"): ("Data_Structure", 30, 0, "The organization of information."),
    ("computer", "metal"): ("Hardware", 20, 10, "The physical shell of thought."),
    ("software", "software"): ("Operating_System", 40, 5, "The manager of the machine."),
    ("internet", "logic"): ("Protocol", 35, 2, "The rules of digital conversation."),
    ("screen", "logic"): ("User_Interface", 30, 0, "The bridge between human and data."),
    ("user_interface", "software"): ("Application", 40, 5, "Software with a purpose."),

    # --- TIER 3: AEROSPACE & TELECOM (EXPANDED) ---
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
    
    # NEW AEROSPACE LATERALS (The "Component" layer)
    ("vacuum", "glass"): ("Vacuum_Seal", 10, 2, "A perfect barrier against the void."),
    ("propulsion", "petroleum"): ("Rocket_Fuel", 30, 45, "Highly refined explosive propellant."),
    ("satellite", "telegraph"): ("Radio_Relay", 40, 5, "Bouncing signals across the horizon."),
    ("guidance_system", "software"): ("Autopilot", 45, 5, "Machine-led navigation."),
    ("aluminum", "glass"): ("Cockpit", 25, 5, "A pressurized window into the sky."),
    ("radio_relay", "internet"): ("Satellite_Broadband", 60, 15, "Global connectivity without wires."),
    ("space_station", "botany"): ("Space_Garden", 55, -10, "Testing life’s resilience in zero-G."),

    # --- TIER 4: BIOTECH & HUMAN ELEMENT (EXPANDED) ---
    ("logic", "dna"): ("Bioinformatics", 50, 5, "Mapping the code of life."),
    ("bioinformatics", "dna"): ("CRISPR", 65, 15, "Genetic editing tools."),
    ("microchip", "dna"): ("Neural_Link", 70, 25, "Direct brain-computer connection."),
    ("neural_link", "logic"): ("Artificial_Consciousness", 90, 40, "A mind without a body."),
    ("dna", "electricity"): ("Electrophoresis", 30, 5, "Analyzing genetic material."),
    ("bioinformatics", "software"): ("Vaccine_Synthesis", 60, -20, "Rapid response to pathogens."),
    ("neural_link", "software"): ("Virtual_Reality", 45, 10, "Digital worlds for the mind."),
    ("microchip", "metal"): ("Robotics", 50, 15, "Programmable mechanical labor."),
    ("robotics", "dna"): ("Cyborg", 80, 30, "The blurring of biology and machine."),
    ("logic", "dna"): ("Biomimicry", 40, -10, "Nature-inspired engineering."),

    # NEW BIOTECH LATERALS (The "Foundation" layer)
    ("dna", "petroleum"): ("Synthetic_Protein", 35, 10, "Artificial building blocks of life."),
    ("robotics", "logic"): ("Actuator", 25, 5, "Precision movement for machines."),
    ("actuator", "prosthetics"): ("Bionic_Limb", 60, 10, "High-fidelity physical replacement."),
    ("dna", "glass"): ("Petri_Dish", 10, 2, "The canvas of the microbiologist."),
    ("petri_dish", "plankton"): ("Bio_Culture", 20, -5, "Controlled growth of microorganisms."),
    ("bio_culture", "ethics"): ("Stem_Cell_Research", 55, 0, "The ethical study of life’s origins."),
    ("crispr", "ethics"): ("Genetic_Policy", 50, -30, "The rules for rewriting nature."
   
    # --- TIER 5: ENERGY REVOLUTION (EXPANDED) ---
    ("sunlight", "silicon"): ("Solar_Panel", 40, 5, "Capturing photons for power."),
    ("solar_panel", "wire"): ("Solar_Farm", 50, 10, "Large scale clean energy."),
    ("logic", "electricity"): ("Algorithm", 20, 0, "Mathematical steps for solving problems."),
    ("algorithm", "software"): ("AI", 60, 20, "Intelligence exhibited by machines."),
    ("ai", "solar_farm"): ("Smart_Grid", 70, -20, "Optimized energy distribution."),
    ("uranium", "logic"): ("Nuclear_Fission", 80, 40, "Splitting the atom."),
    ("nuclear_fission", "steam_engine"): ("Nuclear_Reactor", 85, 30, "Carbon-free, high-risk power."),
    ("sunlight", "vacuum"): ("Solar_Sail", 75, 5, "Propulsion via light pressure."),
    
    # NEW ENERGY LATERALS (The "Sustainability" layer)
    ("uranium", "water"): ("Heavy_Water", 30, 10, "A moderator for nuclear stability."),
    ("uranium", "ethics"): ("Nuclear_Non-Proliferation", 100, -80, "The choice to use the atom for peace."),
    ("coal", "electricity"): ("Power_Plant", 30, 45, "Reliable but dirty energy."),
    ("hydro_turbine", "logic"): ("Variable_Flow_Control", 25, -5, "Smart management of water energy."),
    ("battery", "solar_panel"): ("Energy_Storage", 45, 10, "Holding the sun for the night."),

    # --- TIER 6: CONSEQUENCES (EXPANDED - The "Antagonist" elements) ---
    ("automobile", "petroleum"): ("Greenhouse_Gas", 0, 50, "Atmospheric warming."),
    ("greenhouse_gas", "water"): ("Ocean_Acidification", 0, 60, "Lowering the pH of the seas."),
    ("computer", "metal"): ("E-Waste", 0, 45, "Discarded electronic circuitry."),
    ("plastic", "water"): ("Microplastics", 0, 55, "Tiny particles infiltrating the food chain."),
    ("satellite", "rocket"): ("Space_Debris", 0, 40, "Orbital junk threatening launches."),
    ("ai", "internet"): ("Deepfake", 0, 35, "Synthetic media for misinformation."),
    ("internet", "logic"): ("Privacy_Erosion", 0, 40, "The loss of the personal sphere."),
    
    # NEW CONSEQUENCE LATERALS (The "Systemic Failure" layer)
    ("power_plant", "coal"): ("Smog", 0, 40, "Toxic air in industrial hubs."),
    ("nuclear_reactor", "degradation"): ("Meltdown", 0, 500, "A catastrophic failure of containment."),
    ("e-waste", "clay"): ("Heavy_Metal_Leaching", 0, 70, "Toxins seeping into the groundwater."),
    ("algorithm", "privacy_erosion"): ("Surveillance_State", 0, 150, "Total monitoring of the population."),
    ("microplastics", "plankton"): ("Bioaccumulation", 0, 80, "Toxins moving up the food chain."),

   # --- TIER 7: THE HEALERS (EXPANDED - Remediation) ---
    ("ai", "greenhouse_gas"): ("Carbon_Capture", 50, -60, "Technological CO2 removal."),
    ("robotics", "e-waste"): ("Automated_Recycling", 45, -50, "Machines reclaiming materials."),
    ("bioinformatics", "microplastics"): ("Plastic_Eating_Bacteria", 60, -70, "Biological solution to pollution."),
    ("smart_grid", "greenhouse_gas"): ("Emission_Reduction", 55, -40, "Efficiency mitigating impact."),
    ("ethics", "ai"): ("Alignment", 70, -30, "Ensuring AI serves humanity."),
    ("ethics", "internet"): ("Digital_Rights", 50, -40, "Protecting users in the cloud."),
    
    # NEW HEALER LATERALS (The "Restoration" layer)
    ("carbon_capture", "algae"): ("Bio-Sequestration", 65, -100, "Using engineered life to heal the atmosphere."),
    ("automated_recycling", "steel"): ("Circular_Economy", 80, -120, "A system where waste is a resource."),
    ("digital_rights", "cryptography"): ("Decentralized_Identity", 55, -20, "Owning your soul in the digital age."),
    ("alignment", "surveillance_state"): ("Democratic_AI", 90, -150, "Breaking the chains of total monitoring."),
    ("bioremediation", "ocean_acidification"): ("Coral_Regeneration", 75, -80, "Healing the chemical balance of the reefs."),

    # --- TIER 8: FUTURE SPECULATION (EXPANDED - Quantum & Space) ---
    ("logic", "vacuum"): ("Quantum_Computing", 90, 15, "Computing with subatomic states."),
    ("quantum_computing", "ai"): ("Superintelligence", 150, 50, "Intelligence beyond human grasp."),
    ("nuclear_fission", "sunlight"): ("Nuclear_Fusion", 120, 5, "The power of the stars on Earth."),
    ("robotics", "vacuum"): ("Asteroid_Mining", 100, 20, "Sourcing metals from space."),
    ("synthetic_biology", "carbon_capture"): ("Terraforming", 140, -80, "Making other worlds habitable."),
    
    # NEW FUTURE LATERALS (The "Post-Scarcity" layer)
    ("quantum_computing", "cryptography"): ("Post-Quantum_Security", 110, 0, "Encryption that cannot be broken."),
    ("nuclear_fusion", "electricity"): ("Infinite_Energy", 200, -50, "The end of the resource wars."),
    ("asteroid_mining", "aluminum"): ("Space_Industrialization", 120, 30, "Moving the heavy smoke off-planet."),
    ("superintelligence", "synthetic_biology"): ("Molecular_Assembler", 180, 10, "Building anything atom by atom."),
    ("molecular_assembler", "infinite_energy"): ("Post-Scarcity", 250, -200, "A world where want no longer exists."),

    # --- TIER 9: TRANSCENDENTAL HUB (The Final 500+ Push) ---
    ("superintelligence", "ethics"): ("Singularity", 200, -100, "The point where progress becomes infinite and controlled."),
    ("terraforming", "singularity"): ("Galactic_Civilization", 500, -500, "Spreading life and logic across the stars."),
    ("post-scarcity", "ethics"): ("Utopia", 300, -300, "A society freed from the struggle for survival."),
    ("neural_link", "superintelligence"): ("Mind_Uploading", 150, 50, "Digitizing consciousness into the infinite grid."),
    
    # NEW TRANSCENDENTAL LATERALS (The "Evolutionary" layer)
    ("mind_uploading", "vacuum"): ("Deep_Space_Probe", 200, 10, "A digital mind traveling the cosmos for eons."),
    ("galactic_civilization", "nuclear_fusion"): ("Dyson_Sphere", 400, -50, "Capturing the total output of a star."),
    ("utopia", "synthetic_biology"): ("Biological_Immortality", 350, -100, "Defeating the final bug in the code: death."),
    ("biological_immortality", "mind_uploading"): ("Universal_Identity", 450, 0, "The ability to exist in any form, biological or digital."),
    
    # --- THE FINAL ASCENT: SELF-ACTUALIZATION ---
    ("universal_identity", "ethics"): ("Collective_Wisdom", 600, -600, "The sum of all experience used for the good of all."),
    ("collective_wisdom", "singularity"): ("Cosmic_Harmony", 800, -800, "Total synchronization of energy, life, and thought."),
    
    # THE ULTIMATE ELEMENT
    ("cosmic_harmony", "philosophy"): ("Self-Actualization", 1000, -1000, "The realization of the highest potential; the system is complete."),
    
    # --- BACK-FILL COMBINATIONS (To ensure 500+ density) ---
    ("dyson_sphere", "internet"): ("The_Omega_Network", 500, 0, "A communication system spanning light-years."),
    ("molecular_assembler", "dna"): ("Organic_Printing", 150, -20, "Growing physical structures like bone and wood."),
    ("quantum_computing", "philosophy"): ("Digital_Ontology", 120, 0, "Proving the nature of reality through calculation."),
    ("post-scarcity", "global_travel"): ("Teleportation", 300, -50, "Instantaneous movement through the fold."),
    ("teleportation", "vacuum"): ("Wormhole_Navigation", 450, 20, "Bridging distant galaxies."),
}

# Base elements that can't be created but are used for starting
STARTING_ELEMENTS = {"electricity", "metal", "logic", "vacuum", "sand", "petroleum", "fire", "water", "dna", "sunlight", "uranium", "coal", "ethics"}

