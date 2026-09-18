package data.scripts.world;

import com.fs.starfarer.api.Global;
import com.fs.starfarer.api.campaign.FactionAPI;
import com.fs.starfarer.api.campaign.RepLevel;
import com.fs.starfarer.api.campaign.SectorAPI;
import com.fs.starfarer.api.campaign.SectorGeneratorPlugin;

public class UNSCWorldGen implements SectorGeneratorPlugin {
    private static final String NEX_CORVUS_MODE_MEMKEY = "$nex_corvusMode";

    @Override
    public void generate(SectorAPI sector) {
        // Nex Gate for scripted world generation:
        // - Without Nexerelin, always generate Epsilon Eridani.
        // - With Nexerelin, generate it only in Corvus/vanilla-sector mode.
        //
        // Nexerelin's ExerelinNewGameSetup calls SectorManager.setCorvusMode()
        // before mod onNewGame callbacks run. That setter writes the mode to the
        // sector memory key "$nex_corvusMode". Reading that key uses only the
        // Starsector API, avoiding both a hard Nex class dependency and Java
        // reflection (which Starsector's script sandbox blocks).
        boolean haveNexerelin = Global.getSettings().getModManager().isModEnabled("nexerelin");
        boolean generateScriptedSystem = !haveNexerelin
                || sector.getMemoryWithoutUpdate().getBoolean(NEX_CORVUS_MODE_MEMKEY);

        if (generateScriptedSystem) {
            new UNSCStar().generate(sector);
            initFactionRelationships(sector);
        }
    }

    public static void initFactionRelationships(SectorAPI sector) {
        FactionAPI UNSC = sector.getFaction("unsc");

        UNSC.setRelationship("persean", RepLevel.FAVORABLE);
        UNSC.setRelationship("independent", RepLevel.FAVORABLE);
        UNSC.setRelationship("tritachyon", RepLevel.FAVORABLE);
        UNSC.setRelationship("hegemony", RepLevel.SUSPICIOUS);
        UNSC.setRelationship("luddic_church", RepLevel.SUSPICIOUS);
        UNSC.setRelationship("pirates", RepLevel.HOSTILE);
        UNSC.setRelationship("luddic_path", RepLevel.HOSTILE);
    }
}
