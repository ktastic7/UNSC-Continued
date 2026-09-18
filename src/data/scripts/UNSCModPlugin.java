package data.scripts;

import com.fs.starfarer.api.BaseModPlugin;
import com.fs.starfarer.api.Global;
import com.fs.starfarer.api.impl.campaign.shared.SharedData;
import data.scripts.campaign.UNSCColonyNamer;
import data.scripts.world.UNSCWorldGen;

public class UNSCModPlugin extends BaseModPlugin {

    @Override
    public void onNewGame() {
        SharedData.getData().getPersonBountyEventData().addParticipatingFaction("unsc");
        initUNSC();
    }

    private static void initUNSC() {
        new UNSCWorldGen().generate(Global.getSector());
    }

    @Override
    public void onGameLoad(boolean newGame) {
        // "Nex Gate": the colony-naming feature is only installed when
        // Nexerelin is actually enabled. Non-Nex games do no extra scanning.
        if (!Global.getSettings().getModManager().isModEnabled("nexerelin")) {
            return;
        }

        // Transient: re-added each load, but never serialized into the save.
        // All long-lived state is stored in market memory/sector persistentData.
        if (!Global.getSector().hasTransientScript(UNSCColonyNamer.class)) {
            Global.getSector().addTransientScript(new UNSCColonyNamer());
        }
    }
}
