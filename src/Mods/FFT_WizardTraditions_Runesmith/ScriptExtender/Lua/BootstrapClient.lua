modGuid = "080edc42-9ec0-446f-a9c2-792d5bdf4686"
subClassGuid = "440bfc05-aba4-4b25-a577-172acf5cf0a9"

if Ext.Mod.IsModLoaded("67fbbd53-7c7d-4cfa-9409-6d737b4d92a9") then
    local subClasses = {
        FierroFRunesmith = {
            modGuid = modGuid,
            subClassGuid = subClassGuid,
            class = "wizard",
            subClassName = "Runesmith"
        }
    }

    local function OnSessionLoaded()
        Mods.SubclassCompatibilityFramework.Api.InsertSubClasses(subClasses)
    end

    Ext.Events.SessionLoaded:Subscribe(OnSessionLoaded)
end
