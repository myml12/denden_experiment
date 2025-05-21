library ieee;
use ieee.std_logic_1164.all;

entity PulseGen01 is
  port (
    CLKIN  : in std_logic;
    RSTIN  : in std_logic;
    PLSOUT : out std_logic
  );
end PulseGen01;

architecture Some_Description of PulseGen01 is
  signal C_CNT : integer range 0 to 4999999;
begin

  process(CLKIN, RSTIN)
  begin
    if (CLKIN'event and CLKIN = '1') then
      if RSTIN = '0' then 
        C_CNT <= 0;
        PLSOUT <= '0';
      elsif C_CNT = 4999999 then
        C_CNT <= 0;
        PLSOUT <= '1';
      else
        C_CNT <= C_CNT + 1;
        PLSOUT <= '0';
      end if;
    end if;
  end process;

end Some_Description;
