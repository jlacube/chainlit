import React from 'react';
import { useRecoilValue } from 'recoil';

import { composerButtonState } from '@chainlit/react-client';

import { IComposerButton } from '@/types/composerButton';

import CustomComposerButton from './CustomComposerButton';

const CustomComposerButtons: React.FC = () => {
  const composerButtons = useRecoilValue(
    composerButtonState
  ) as IComposerButton[];

  if (!composerButtons || composerButtons.length === 0) {
    return null;
  }

  return (
    <div className="flex gap-1">
      {composerButtons.map((button: IComposerButton) => (
        <CustomComposerButton key={button.id} button={button} />
      ))}
    </div>
  );
};

export default CustomComposerButtons;
