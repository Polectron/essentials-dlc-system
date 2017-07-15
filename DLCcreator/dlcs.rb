def downloadDLC(url)
  string = pbDownloadToString(url)
  data = pbParseJson(string)
  steps = data["steps"]
  counter = 0
  for step in steps
    
    if step["type"] == "tileset"
      tilesets = pbLoadRxData("Data/Tilesets")
      if step["action"] == "add" || step["action"] == "update"
        pbDownloadToFile(step["file"],"Data/tempTilesets.rxdata")
        tempTilesets = pbLoadRxData("Data/tempTilesets")
        tilesets[step["id"]] = tempTilesets[step["id"]]
        save_data(tilesets,"Data/Tilesets.rxdata")
        begin
          File.delete("Data/tempTilesets.rxdata")
        rescue SystemCallError
        end
      end
    end
    
    if step["type"] == "map"
      filename = step["file"].split("/")[-1]
      if step["action"] == "add"
        last = getMapLastOrder()+1
        pbDownloadToFile(step["file"], "Data/"+filename)
        maps = pbLoadRxData("Data/MapInfos")
        map = RPG::MapInfo.new
        map.name = step["name"]
        map.order = last
        maps[step["id"].to_i] = map
        save_data(maps,"Data/MapInfos.rxdata")
      elsif["action"] == "update"
        pbDownloadToFile(step["file"], "Data/"+filename)
      end
    end
    
    if step["type"] == "audio"
      if step["action"] == "add" || step["action"] == "update"
        pbDownloadToFile(step["file"], "Audio/"+step["name"])
      end
    end
    
    if step["type"] == "graphics"
      if step["action"] == "add" || step["action"] == "update"
        pbDownloadToFile(step["file"], "Graphics/"+step["name"])
      end
    end
    
    if step["type"] == "script"
      if step["action"] == "add" || step["action"] == "update"
        content = pbDownloadToString(step["file"])
        pbAddScriptToFile(content, step["name"])
      end
    end
    
    # if step["type"] == "pbs"
      # if step["action"] == "add" || step["action"] == "update"
        # pbDownloadToFile(step["file"], "PBS/"+filename)
      # end
    # end
    
    if step["type"] == "data"
      if step["action"] == "add" || step["action"] == "update"
        pbDownloadToFile(step["file"], "Data/"+step["name"])
      end
    end
    
    if step["type"] == "variable"
        $game_variables[step["id"]] = step["value"]
    end
    
    if step["type"] == "switch"
        game_switches[step["id"]] = step["value"]
    end

    counter += 1
  end
  $DEBUG = true
  #pbImportNewMaps
  msgwindow=Kernel.pbCreateMessageWindow
  pbCompileAllData(true) {|msg| Kernel.pbMessageDisplay(msgwindow,msg,false) }
  Kernel.pbMessageDisplay(msgwindow,_INTL("Se han compilado todos los datos del juego."))
  Kernel.pbDisposeMessageWindow(msgwindow)
  $DEBUG = false
end

def manageDLCs()
  #Kernel.pbMessage(_INTL("{1}",Zlib::Inflate.inflate("x\x9c\xf3\xc8\xcfIT\xc8-\xcdK\xc9W\x04\x00\x17\xe7\x03\xe9")))
  #tilesets=load_data("Data/Tilesets.rxdata")
  #for tileset in tilesets
  #  p tileset
  #end
  string = pbDownloadToString(DLCSURL)
  data = pbParseJson(string)
  dlcs = data["dlcs"]
  stopdownload = false
  
  commands=[]
  list = []
  n = 0

  for dlc in dlcs
    commands.push(dlc["name"])
    n += 1
  end
  commands.push(_INTL("Salir"))
  
  loop do
    command=Kernel.pbShowCommands(nil,commands,-1)
    if command>=0 && command<commands.length-1
      command2=Kernel.pbMessage(_INTL("¿Qué quieres hacer con {1}?",
         dlcs[command]["name"]),[
         _INTL("Descargar"),
         _INTL("Info"),
         _INTL("Cancelar")
         ],-1)
      if command2==0 # Download
        pbFadeOutIn(99999){
          if !$PokemonGlobal.dlcs.include?(command)
            for dependency in dlcs[command]["requires"]
              if !$PokemonGlobal.dlcs.include?(dependency)
                Kernel.pbMessage(_INTL("Es necesario instalar {1} para poder instalar este DLC",dlcs[dependency]["name"]))
                stopdownload = true
              end
            end
            if !stopdownload
              Kernel.pbMessage(_INTL("Descargando"))
              downloadDLC(dlcs[command]["steps"])
              $PokemonGlobal.dlcs.push(command)
              Kernel.pbMessage(_INTL("Guardando..."))
              pbSave
              save_data($PokemonGlobal.dlcs,"Data/dlcs.dat")
            end
          else
            Kernel.pbMessage("Ya tienes instalado este DLC")
          end
        }
      elsif command2==1 # Info
        Kernel.pbMessage(_INTL("{1}",dlcs[command]["description"]))
      elsif command2==2 # Cancel
        
      end
    else
      break
    end
  end
end

def pbAddScriptToFile(script,sectionname)
  begin
    scripts=load_data("Data/Scripts.rxdata")
    scripts=[] if !scripts
  rescue
    scripts=[]
  end
  s=pbFindScript(scripts,sectionname)
  if s
    #s[2]=Zlib::Deflate.deflate("#{script}\r\n")
    s[2]=script.unpack("m")[0]
  else
    tempscript = scripts[scripts.size-1]
    #scripts.push([rand(100000000),sectionname,Zlib::Deflate.deflate("#{script}\r\n")])
    scripts[scripts.size-1] = [rand(100000000),sectionname,script.unpack("m")[0]]
    scripts.push(tempscript)
  end
  save_data(scripts,"Data/Scripts.rxdata")
end

def getMapLastOrder()
  maps = pbLoadRxData("Data/MapInfos")
  last_order = 0
  last_id = 0
  
  for id in maps.keys
    if maps[id].order > last_order
      last_order = maps[id].order
    end
    if id > last_id
      last_id = id
    end    
  end
  
  #Kernel.pbMessage(_INTL("{1} {2} {3}",last_id,maps[id].name,last_order))
  return last_order
end

def reinstallDLCS()
  string = pbDownloadToString(DLCSURL)
  data = pbParseJson(string)
  dlcs = data["dlcs"]
  counter = 0
  for dlc in dlcs
    if $PokemonGlobal.dlcs.include?(counter)
        downloadDLC(dlc["steps"])
    end
    counter += 1
  end
end
