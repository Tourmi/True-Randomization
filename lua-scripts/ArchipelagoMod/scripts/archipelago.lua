require("utils")
require("bloodstainedUtils")

local AP = require("lua-apclientpp")

---@class Archipelago
Archipelago = {
    ---@type APClient
    _client = nil,
    ---@type boolean
    _stopLoop = false
}

local uuid = "018e5998-736f-7718-8448-ee7869eff59e"
local gameName = "Bloodstained Ritual of the Night"
local itemsHandling = 7 -- full remote
local messageFormat = AP.RenderFormat.TEXT

---@return Archipelago
function Archipelago:new()
    local archi = {}
    setmetatable(archi, self)
    self.__index = self
    return archi
end

---@param host string
---@param slotname string
---@param password string
function Archipelago:Start(host, slotname, password)
    function OnSocketConnected()
        ModPrint("OnSocketConnected")
    end

    function OnSocketDisconnected()
        ModPrint("OnSocketDisconnected")
    end

    function OnSocketError(reason)
        ModPrint("Failed to connect for reason: " .. reason)
    end

    function OnRoomInfo()
        ModPrint("Connecting to slot: " .. slotname)
        self._client:ConnectSlot(slotname, password, itemsHandling, { "Lua-APClientPP", "DeathLink" }, { 0, 4, 5 })
    end

    ---comment
    ---@param slot_data { [string] : any }
    function OnSlotConnected(slot_data)
        ModPrint("Connection successful")
    end

    ---@param reasons string[]
    function OnSlotRefused(reasons)
        ModPrint("Connection failed: " .. table.concat(reasons, ", "))
    end

    ---@param networkItems NetworkItem[]
    function OnItemsReceived(networkItems)
        ModPrint("OnItemsReceived")
        for i, networkItem in ipairs(networkItems) do
            local name = self._client:get_item_name(networkItem.item, gameName)
            --TODO translate localized name to FName
            GiveItem(name, 1)
        end
    end

    ---@param dataPackage {[string] : any}
    function OnDataPackageChanged(dataPackage)
        ModPrint("DataPackageChanged")
        -- TODO invalidate cache
    end


    ---@param command {[string] : any}
    function OnBounced(command)
        ModPrint("Bounced")
        if TableContains(command["tags"], "DeathLink") then
            KillPlayer(command["data"]["cause"])
        end
    end

    function OnPrintJson(msg, _)
        ModPrint(self._client:render_json(msg, messageFormat))
    end

    ModPrint("Connecting to " .. host)
    self._client = AP(uuid, gameName, host)

    self._client:set_print_handler(ModPrint)
    self._client:set_print_json_handler(OnPrintJson)
    self._client:set_socket_connected_handler(OnSocketConnected)
    self._client:set_socket_disconnected_handler(OnSocketDisconnected)
    self._client:set_socket_error_handler(OnSocketError)
    self._client:set_room_info_handler(OnRoomInfo)
    self._client:set_slot_connected_handler(OnSlotConnected)
    self._client:set_slot_refused_handler(OnSlotRefused)
    self._client:set_items_received_handler(OnItemsReceived)
    self._client:set_data_package_changed_handler(OnDataPackageChanged)
    self._client:set_bounced_handler(OnBounced)

    self._stopLoop = false
    while not self._stopLoop do
        local t = os.clock() + 0.05
        while t > os.clock() do end
        self._client:poll()
    end
    self._client = nil
    collectgarbage("collect")
end

function Archipelago:Died()
    self._client:Bounce({}, nil, nil, { "DeathLink" })
end

function Archipelago:GotLocation(locationName)
    local locationId = self._client:get_location_id(locationName)
    self._client:LocationChecks({ locationId })
end

function Archipelago:Completed()
    self._client:StatusUpdate(APClient.ClientStatus.GOAL)
end

function Archipelago:Stop()
    self._stopLoop = true
end
