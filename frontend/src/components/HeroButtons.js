import React, { useState, useEffect } from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import { useTheme, useMediaQuery } from "@mui/material";
import InfoIcon from "@mui/icons-material/CardTravel";
import PlayIcon from "@mui/icons-material/PlayCircleOutlineOutlined";
import { getEmployeeProfiles } from "../utils/api";

const HeroButtons = () => {
  const theme = useTheme();
  const isMd = useMediaQuery(theme.breakpoints.up("md"), {
    defaultMatches: true,
  });

  const videoUrl = "/videos/demo.mp4";

  const [profiles, setProfiles] = useState([]);

  const handleClick = async () => {
    const response = await getEmployeeProfiles();
    if (response && response.data) {
      setProfiles(response.data);
    }
  };

  useEffect(() => {
    const watchDemo = () => {
      const videoWindow = window.open(videoUrl, "_blank");
      videoWindow.focus();
    };
    const button = document.getElementById("watch-demo-btn");
    button.addEventListener("click", watchDemo);
    return () => {
      button.removeEventListener("click", watchDemo);
    };
  }, [videoUrl]);

  const renderProfiles = () => {
    return (
      <ul>
        {profiles.map((profile) => (
          <li key={profile.id}>{profile.username}</li>
        ))}
      </ul>
    );
  };

  return (
    <>
      <Box
        display="flex"
        flexDirection={{ xs: "column", sm: "row" }}
        alignItems={{ xs: "stretched", sm: "flex-start" }}
        justifyContent="center"
        marginTop={4}
      >
        <Button
          component="a"
          variant="contained"
          size="large"
          color="primary"
          href="#"
          startIcon={<InfoIcon />}
          fullWidth={isMd ? false : true}
          disableElevation={true}
          sx={{
            marginRight: "15px",
            border: "2px solid transparent",
            "&:hover": {
              backgroundColor: "transparent",
              color: theme.palette.primary.main,
              border: "2px solid " + theme.palette.primary.main,
            },
          }}
          onClick={handleClick}
        >
          Bitácora de viaje
        </Button>
        <Box
          marginTop={{ xs: 2, sm: 0 }}
          marginLeft={{ sm: 1 }}
          width={{ xs: "100%", md: "auto" }}
        >
          <Button
            component="a"
            variant="outlined"
            color="primary"
            size="large"
            href={videoUrl}
            target="_blank"
            rel="noopener noreferrer"
            startIcon={<PlayIcon />}
            fullWidth={isMd ? false : true}
            disableElevation={true}
            sx={{
              marginRight: "15px",
              border: "2px solid " + theme.palette.primary.main,
              "&:hover": {
                backgroundColor: theme.palette.primary.main,
                color: theme.palette.common.white,
                border: "2px solid " + theme.palette.primary.main,
              },
            }}
            id="watch-demo-btn"
          >
            Video Tutorial
          </Button>
        </Box>
      </Box>
      {profiles.length > 0 && renderProfiles()}
    </>
  );
};

export default HeroButtons;
