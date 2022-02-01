import React, { useRef, useState } from "react";
// Import Swiper React components
import { Swiper, SwiperSlide } from "swiper/react/swiper-react.js";

// Import Swiper styles
// import "swiper/css";
// import "swiper/css/pagination";

import 'swiper/swiper-bundle.min.css'
import 'swiper/swiper.min.css'
import 'swiper/modules/pagination/pagination.min.css';
import 'swiper/modules/mousewheel/mousewheel.min.css';


import Challenge from './Challenge.jsx';
import TextInput from './TextInput.jsx';
import Tasks from './Tasks.jsx';

// import "./styles.css";

// import required modules
// import { Mousewheel, Pagination } from "swiper";
import { Keyboard, Pagination, Navigation } from "swiper";

export default function App() {
  return (
    <>
      <Swiper
        slidesPerView={1}
        spaceBetween={30}
        keyboard={{
          enabled: true,
        }}
        pagination={{
          clickable: true,
        }}
        navigation={true}
        modules={[Keyboard, Pagination, Navigation]}
        className="mySwiper"
      >
        <SwiperSlide>
            <TextInput label={"Challenge Title"}/>
        </SwiperSlide>
        <SwiperSlide>
            <TextInput label={"Challenge Description"}/>
        </SwiperSlide>
        <SwiperSlide>
            <Tasks />
        </SwiperSlide>
      </Swiper>
    </>
  );
}

// export default function App() {
//   return (
//     <>
//       <Swiper
//         direction={"vertical"}
//         slidesPerView={5}
//         spaceBetween={10}
//         mousewheel={true}
//         pagination={{
//           clickable: true,
//         }}
//         modules={[Mousewheel, Pagination]}
//         className="mySwiper"
//         onSlideChange={() => console.log("slide change")}
//         onSwiper={swiper => console.log(swiper)}
//       >
//         <SwiperSlide style={{backgroundColor: 'red', height: '100%'}}><Challenge /></SwiperSlide>
//         <SwiperSlide style={{backgroundColor: 'yellow'}}><Challenge /></SwiperSlide>
//         <SwiperSlide style={{backgroundColor: 'green'}}>Slide 4</SwiperSlide>
//         <SwiperSlide style={{backgroundColor: 'pink'}}>Slide 5</SwiperSlide>
//         <SwiperSlide style={{backgroundColor: 'orange'}}>Slide 6</SwiperSlide>
//         <SwiperSlide>Slide 7</SwiperSlide>
//         <SwiperSlide>Slide 8</SwiperSlide>
//         <SwiperSlide>Slide 9</SwiperSlide>
//       </Swiper>
//     </>
//   );
// }
