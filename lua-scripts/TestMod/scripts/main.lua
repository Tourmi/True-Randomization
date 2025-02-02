local UEHelpers = require("UEHelpers")
require("utils")
require("bloodstainedUtils")

Print("Loading mod")

local lastLocation = nil

function MessagePlayer(message)
    local gameInstance = GetGameInstance()
    gameInstance:OCMsg(message, 5)
end

function ReadPlayerLocation()
    local FirstPlayerController = UEHelpers:GetPlayerController()
    local Pawn = FirstPlayerController.Pawn
    local Location = Pawn:K2_GetActorLocation()
    MessagePlayer(string.format("Player location: {X=%.3f, Y=%.3f, Z=%.3f}", Location.X, Location.Y, Location.Z))
    if lastLocation then
        MessagePlayer(string.format("Player moved: {delta_X=%.3f, delta_Y=%.3f, delta_Z=%.3f}",
            Location.X - lastLocation.X,
            Location.Y - lastLocation.Y,
            Location.Z - lastLocation.Z)
        )
    end

    lastLocation = Location
end

function Test()
    ---@type APlayerController
    local playerController = UEHelpers:GetPlayerController()
    Print(FText("asdf"))
    Print(FName("SummonButt"))

    ---@type APBInterfaceHUD
    local hud = FindFirstOf("PBInterfaceHUD")

    ---@type UShortcutSlotMenu_C
    local shortcutslotMenu = FindFirstOf("ShortcutSlotMenu_C")
    shortcutslotMenu.Index = 9

    ---@type UShortcutExecMenu_C
    local shortcutExecMenu = FindFirstOf("ShortcutExecMenu_C")
    shortcutExecMenu:DecideEquipment()

    local Pawn = playerController.Pawn
    local Location = Pawn:K2_GetActorLocation()
    ---@type UPBGameInstance
    local gameInstance = GetGameInstance()
    MessagePlayer("Please connect to Archipelago using the console (F10): /connect ip:host slotName password")
    local player = gameInstance:GetPlayerCharacter(0)
    player:FlipRotation()

    gameInstance:NextRoomStartTimer(2)

    --gameInstance.CurrentBoss:EndBossBattle()
    --gameInstance.pRoomManager:Warp(FName("m09TRN_003"), true, true, FName("None"), { A = 1, R = 0, G = 0, B = 0 })
    --local playerStart = FindFirstOf("PlayerStart")
    --gameInstance.CurrentBoss:WarpToPlayerStart(playerStart)
    --local playerState = gameInstance:GetPlayerState(0)

    ---@type UPBCharacterInventoryComponent
    local characterInventory = FindFirstOf("PBCharacterInventoryComponent")
    --characterInventory:GetItemWithDisplay(FName("Poison"), 3, false)
    --characterInventory:UseConsumable(FName("Waystone"), false)
    characterInventory:GetItemWithDisplay(FName("NeverSatisfied"), 1, false)
    --FindFirstOf("PBShardManager"):CallShardAnimation(player, FName("NeverSatisfied"), 10 --[[EGameCommonFlag.GotShard]], Location)
end

function Init()
    Print("Trying to init")
    if (not FindFirstOf("ItemGetPopup_C"):IsValid()) then
        Print("Save not loaded, trying again in 5 seconds")
        ExecuteWithDelay(5000, Init)
        return
    end

    RegisterHook("/Game/Core/UI/Common/Popup/PopupAsset/ItemGetPopup.ItemGetPopup_C:Initialize", function(self)
        ---@type UItemGetPopup_C
        local popup = self:get()
        ExecuteInGameThread(function()
            Print("Got item: " .. popup.MLTF_SIZE_23_ItemName.text:ToString())
        end)
    end)

    RegisterConsoleCommandGlobalHandler("/test", function(Cmd, CommandParts, Ar)
        Print(Cmd)
        Print(CommandParts[1])
        Print(CommandParts[2])
        Print(CommandParts[3])
        return true
    end)

    Print("Init complete")
end

RegisterKeyBind(Key.F1, function()
    ExecuteInGameThread(function()
        ReadPlayerLocation()
    end)
end)

RegisterKeyBind(Key.F2, function()
    ExecuteInGameThread(function()
        Test()
    end)
end)

RegisterKeyBind(Key.F3, function()
    ExecuteInGameThread(function()
        ---@type UShortcutSlotMenu_C
        local shortcutslotMenu = FindFirstOf("ShortcutSlotMenu_C")
        shortcutslotMenu.Index = 9

        ---@type UShortcutExecMenu_C
        local shortcutExecMenu = FindFirstOf("ShortcutExecMenu_C")
        shortcutExecMenu:DecideEquipment()
    end)
end)
Print("Mod loaded")

Init()
