local gameInstance = FindFirstOf("PBGameInstance")

NotifyOnNewObject("/Script/ProjectBlood.TutorialWidgetBase", function(ConstructedObject)
	if GetClassName(ConstructedObject) == "TutorialShardWindow_C" then
		local shardWindowClosePreHook, shardWindowClosePostHook
		shardWindowClosePreHook, shardWindowClosePostHook = RegisterHook("/Game/Core/UI/Tutorialv2/TutorialShardWindow.TutorialShardWindow_C:OnCloseWindow", function()
			CheckBossSoftlock()
			UnregisterHook("/Script/ProjectBlood.PBLoadingManager:ShowLoadingScreen", shardWindowClosePreHook, shardWindowClosePostHook)
		end)
	end
end)

function CheckBossSoftlock()
    local currentBoss = gameInstance.CurrentBoss
    if currentBoss:IsValid() then
        local bossName = currentBoss:GetBossId():ToString()
        if IsInList({"N1003", "N2001", "N2013"}, bossName) and currentBoss:GetHitPoint() <= 0 then
            ExecuteInGameThread(function() currentBoss:EndBossBattle() end)
        end
        if bossName == "N2001" then
            ExecuteWithDelay(2000, function() gameInstance.pRoomManager:Warp(FName("m09TRN_003"), true, true, FName("None"), {}) end)
        end
    end
end

function GetClassName(object)
	return SplitString(object:GetFullName(), " ")[1]
end

function IsInList(list, item)
    for index = 1,#list,1 do
        if list[index] == item then return true end
    end
    return false
end

function SplitString(inString, separator)
	local list = {}
	for subString in string.gmatch(inString, "([^"..separator.."]+)") do
		table.insert(list, subString)
	end
	return list
end